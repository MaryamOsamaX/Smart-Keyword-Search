import RAKE
import TextRank

def addUnique(bigList,addedList):
    for i in addedList:
        if i not in bigList:
            bigList.append(i)

def get_PageKewords(article):
    listOfKeywords_1 =RAKE.get_RAKE(article)
    listOfKeywords_2 = TextRank.get_TextRank(article)
    pageKeywords = []
    addUnique(pageKeywords,listOfKeywords_1)
    addUnique(pageKeywords, listOfKeywords_2)
    return pageKeywords

if __name__ == '__main__':
    g=[]
    a=['a','b','1']
    b=['1','2','3']
    addUnique(g,a)
    print(g)
    addUnique(g,b)
    print(g)