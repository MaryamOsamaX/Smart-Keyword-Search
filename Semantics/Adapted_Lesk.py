#!pip install pywsd==1.2.4
# Python Word Sense Disambiguation (pyWSD)

from nltk.corpus import stopwords
from itertools import chain
from pywsd.tokenize import word_tokenize
from pywsd.utils import lemmatize, porter, lemmatize_sentence, synset_properties

pywsd_stopwords = [u"'s", u"``", u"`"]
EN_STOPWORDS = set(stopwords.words('english') + list(string.punctuation) + pywsd_stopwords)

def synsetSignatures(ss: "wn.Synset"):
    signature = []
    # Adds the definition, example sentences and lemma_names.
    signature += word_tokenize(ss.definition())
    signature += chain(*[word_tokenize(eg) for eg in ss.examples()])
    signature += ss.lemma_names()
    
    # Includes lemma_names of hyper-/hyponyms.
    hyperhyponyms = set(ss.hyponyms() + ss.hypernyms() + ss.instance_hyponyms() + ss.instance_hypernyms())
    signature += set(chain(*[i.lemma_names() for i in hyperhyponyms]))
    
    # Includes signatures from related senses as in Adapted Lesk.
    # Includes lemma_names from holonyms, meronyms and similar_tos
    related_senses = set(ss.member_holonyms() + ss.part_holonyms() + ss.substance_holonyms() + \
                             ss.member_meronyms() + ss.part_meronyms() + ss.substance_meronyms() + \
                             ss.similar_tos())
    signature += set(chain(*[i.lemma_names() for i in related_senses]))
    # Lowercase.
    signature = set(s.lower() for s in signature) 

    # Removes stopwords.
    signature = set(signature).difference(EN_STOPWORDS) 
    
    # Lemmatized context is preferred over stemmed context.
    signature = [lemmatize(s) for s in signature]
    # Keep only the unique bag-of-words
    return set(signature)

def getSignaturesForWord(ambiguous_word: str, pos: str = None) -> dict:
    

    # Ensure that the POS is supported.
    pos = pos if pos in ['a', 'r', 's', 'n', 'v', None] else None
     
    # If the POS specified isn't found but other POS is in wordnet.
    if not wn.synsets(ambiguous_word, pos) and wn.synsets(ambiguous_word):
        pos = None
    
    # Holds the synset->signature dictionary.
    ss_sign = {}
    for ss in wn.synsets(ambiguous_word, pos):
        ss_sign[ss] = synsetSignatures(ss)
    
    # Matching exact words may cause sparsity, so optional matching for stems.
    # Not advisible to use thus left out of the synsets_signatures()
    ss_sign = {ss:[porter.stem(s) for s in signature]
                   for ss, signature in ss_sign.items()}
    
    return ss_sign
    

def compare_overlaps_greedy(context: list, synsets_signatures: dict) -> "wn.Synset":
    max_overlaps = 0; lesk_sense = None
    for ss in synsets_signatures:
        overlaps = set(synsets_signatures[ss]).intersection(context)
        
        if len(overlaps) > max_overlaps:
            lesk_sense = ss
            max_overlaps = len(overlaps)
            
                    

            
    #print(lesk_sense)
    return lesk_sense
    
def adapted_lesk(context_sentence: str, ambiguous_word: str,pos: str = None) -> "wn.Synset":
   
    # Ensure that ambiguous word is a lemma.
    ambiguous_word = lemmatize(ambiguous_word)
    
    # If ambiguous word not in WordNet return None
    if not wn.synsets(ambiguous_word):
        return None
    
    # Get the signatures for each synset.
    ss_sign = getSignaturesForWord(ambiguous_word, pos=pos)
    # Disambiguate the sense in context.
    
    lemmatize_sentence(context_sentence)
    context_sentence = context_sentence.split()
    return compare_overlaps_greedy(context_sentence, ss_sign)
    
