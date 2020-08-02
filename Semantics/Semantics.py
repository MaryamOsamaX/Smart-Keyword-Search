from Semantics.Adapted_Lesk import *
from Semantics.Functions import *
from nltk.corpus import wordnet as wn
import requests 
        
#from wordNet
def getSynonymsAndRelatedKeyword(synset, lch_threshold=2.26):
    res=[]
    for net in wn.all_synsets():
        try:
            lch = wn.lch_similarity(synset ,net)
            # The value to compare the LCH to was found empirically.
            # (The value is very application dependent. Experiment!)
            if lch >= lch_threshold:
                 for word in net.lemmas():
                        res.append((word.name() , lch))
                        
        except:
                continue
          
    return res


#from conceptNet
def getWordsByConceptNet(imbg_word , pos):
    words=[]
    relations=['Synonym','RelatedTo','HasContext','SimilarTo','IsA','PartOf','HasA',
               'AtLocation','HasSubevent','HasFirstSubevent','HasLastSubevent','HasPrerequisite',
               'HasProperty','CreatedBy','DistinctFrom','DerivedFrom','DefinedAs','MannerOf','LocatedNear']

    for r in relations:
        response = requests.get('http://api.conceptnet.io/query?node=/c/en/'+imbg_word+'/'+pos+'&other=/c/en&rel=/r/'+r)
        obj = response.json()

        for edge in obj['edges']:
            if edge['end']['label'] == imbg_word:
                words.append((edge['start']['label'] ,edge['weight']))

            else:
                words.append((edge['end']['label'],edge['weight']))

    return sort(removeDuplicate(words))
    
    
def getSemanticsForSentence(sen , keyword):
    senToken=sen.split()
    SentenceWords=[]
    KeywordList=keyword.split()
    
    for word in KeywordList:
        i=0
        for w in senToken:
            if(w!= word):
                i+=1
            else:
                pos=getPos(sen , i)
                print(pos)
                if (pos != None):
                    sense=adapted_lesk(sen , w , pos)
                    wordsNet=getSynonymsAndRelatedKeyword(sense)
                    wordsNet=sort(wordsNet)
                    wordsNet=cleanData(wordsNet)
                    
                    wordsConcept=getWordsByConceptNet(w , pos)
                    allWords= removeDuplicate(wordsNet + wordsConcept )
                    SentenceWords.append(allWords)
                else:
                    SentenceWords.append(w) 
                i+=1
    return SentenceWords
    
#input format -> ["coronavirus" , "pagerank implementation"] , text

def getSemanticForAllKeyWords(keywordsList ,text):
    #
    #....
    #
    return [["covid-19", "COV19" , "Sars"] , ["pagerank executation" , "pagerank effectuation"]]
    
    

    
        

        
        
        
        
    
    