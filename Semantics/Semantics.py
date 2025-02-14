from Semantics.Adapted_Lesk import *
from Semantics.Functions import *
from nltk.corpus import wordnet as wn
from googletrans import Translator
import requests 
import json
import itertools
        
#from wordNet
def getSynonymsAndRelatedKeyword(synset,oneWord ,  lch_threshold=2.26):
    res=[]
    #print(synset)
    if (oneWord== True):
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
    else:
        if synset:
            for l in synset.lemmas():
                res.append((l.name(),1))

    return res


#from conceptNet
def getWordsByConceptNet(imbg_word ,oneWord ,pos):
    words=[]
    relations=['Synonym','RelatedTo','HasContext','SimilarTo','IsA','PartOf','HasA',
               'AtLocation','HasSubevent','HasFirstSubevent','HasLastSubevent','HasPrerequisite',
               'HasProperty','CreatedBy','DistinctFrom','DerivedFrom','DefinedAs','MannerOf','LocatedNear']
    
    for r in relations:
        response = requests.get('http://api.conceptnet.io/query?node=/c/en/'+imbg_word+'/'+pos+'&other=/c/en&rel=/r/'+r)
        obj = response.json()

        for edge in obj['edges']:
            wordFromList1 = wn.synsets(imbg_word)
            wordFromList2 = wn.synsets(edge['start']['label'])
            if edge['end']['label'] == imbg_word :
                words.append((edge['start']['label'] ,edge['weight']))

            else:
                words.append((edge['end']['label'],edge['weight']))
        if(oneWord!=True):
            break

    return sort(removeDuplicate(words))
    
    
def getSynonymsMerriamWebster(word , pos):
    api_token = '6a21f8ce-b84a-4fdd-a4fa-0b94a0a1f78d'
    api_url_base = 'https://www.dictionaryapi.com/api/v3/references/ithesaurus/json/'+word+'?key='+api_token

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
        }
    response = requests.request("POST", api_url_base,headers=headers)
    data = response.json()
    syns=[]
    if(isinstance(data[0] , dict)):
        for d in data:
            if(d['fl']==pos):
                for m in d['meta']['syns']:
                    for w in m:
                        syns.append(w)
    return syns
    
    
def getSemanticsForSentence(sen , keyword):
    senToken=sen.split()
    SentenceWords=[]
    wordsNet=[]
    KeywordList=keyword.split()
    
    for word in KeywordList:
        i=0
        for w in senToken:
            if(w!= word):
                i+=1
            else:
                pos=getPos(sen , i)
                # print(w)
                # print(pos)
                if (pos != None):
                    if(len(wn.synsets(w))!=0):
                        #print(wn.synsets(w))
                        sense=adapted_lesk(sen , w , pos)

                        if(len(KeywordList)!=1):
                            wordsNet=getSynonymsAndRelatedKeyword(sense ,False)
                        else:
                            wordsNet=getSynonymsAndRelatedKeyword(sense ,True)
                    
                        wordsNet=sort(wordsNet)
                        wordsNet=cleanData(wordsNet)
                      
                    
                    if(len(KeywordList)!=1):
                        wordsConcept=getWordsByConceptNet(w ,False, pos)
                    else:
                        wordsConcept=getWordsByConceptNet(w ,True, pos)
                    
                    '''  
                    for Adding Merriam-Webster API
                    posM=''
                    if  (pos=='n'): posM+='noun' 
                    elif(pos=='v'): posM+='verb'
                    elif(pos=='a'): posM+='adjective'
                    else :          posM+='adverb'
                    synMW=getSynonymsMerriamWebster(w ,posM)
                    ''' 
                   
                    allWords= removeDuplicate([(w,1)]+ wordsNet +wordsConcept)
                    SentenceWords.append(allWords)
        
                    
                    wordsNet=[]
                else:
                    SentenceWords.append([(w,1)]) 
                i+=1
    ok =list(itertools.product(*SentenceWords))
    sem=[]
    for t in ok:
        r=""
        for w in t:
            r+=" "
            r+=w[0]
        sem.append(r)
    
    return sem
    

def paraphrasingKeywords(keywordList):
    languages=["ko","ja","es","ar","it","ga" ,"fr","de" ,"cs","bg","hr","el","pt","no","ru","ro",
              "th" ,"sv","nl","pl"]
    translator = Translator()
    allBackTranslated=[]
    for lang in languages:
        translation=translator.translate(keywordList, dest=lang)
        translated=[]
        for t in translation:
            translated.append(t.text)
        translation=translator.translate(translated, src=lang)
        backTraslated=[]
        for t in translation:
            backTraslated.append(t.text.lower())
        allBackTranslated.append(backTraslated)
        finalRes=[]
        for i in range(0 , len(allBackTranslated[0])):
            temp=[]
            for a in allBackTranslated:
                temp.append(a[i])
            finalRes.append(list(set(temp)))
            
    return finalRes
    
#input format -> ["coronavirus" , "pagerank implementation"] , text
def getSemanticForAllKeyWords(keywordsList , text):
    allSemantics=[]
    A= keywordsList[:len(keywordsList)//2]
    B = keywordsList[len(keywordsList)//2:]
    paraphrases=[]
    A=paraphrasingKeywords(A)
    B=paraphrasingKeywords(B)
    paraphrases=A+B
    i=0
    for word in keywordsList:
        matches=matchSentence(word , text)
        if matches:
            sen=matches[0]
            keywordSematics=getSemanticsForSentence(sen , word)
            allSemantics.append(keywordSematics+paraphrases[i])
        i+=1
        
    
    return allSemantics
    
    

    
        

        
        
        
        
    
    
