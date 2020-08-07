import re
def removeDuplicate(Input):
    seen = set() 
    Output = [(a, b) for a, b in Input 
             if not (a in seen or seen.add(a))] 
    return Output

def last(n):
    return n[-1]  
 
def sort(tuples):
    return sorted(tuples, key=last ,reverse=True)
def cleanData(arr):
    output=[]
    for a,b in arr:
        u=a.replace('-',' ')
        u=u.replace('_',' ')
        output.append((u,b))
    return output
    

import spacy
sp = spacy.load('en_core_web_sm')

def getPos(sentence , wordIndex):
    sen = sp(sentence)
    tag =sen[wordIndex].tag_
    mapp=''
    if tag=='JJ' or tag=='JJR' or tag=='JJS':
        mapp='a'
    elif tag=='NN' or tag=='NNS' or tag=='NNP' or tag=='NNPS':
        mapp='n'
    elif tag=='RB' or tag=='RBR' or tag=='RBS' :
        mapp='r'
    elif tag=='VB' or tag=='VBD' or tag=='VBG' or tag=='VBN' or tag=='VBP' or tag=='VBZ' :
        mapp='v'
    else:
        mapp=None
    return mapp


def matchSentence(query , text):
    matches=re.findall(r'(?:[^ ]+ ){0,10}'+query+'(?: [^ ]+){0,10}',text)
    return matches