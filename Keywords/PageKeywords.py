from Keywords import TextRank, YAKE
from Keywords.RAKE import get_RAKE


def addUnique(bigList,addedList):
    for i in addedList:
        if i not in bigList:
            bigList.append(i)

def get_PageKewords(article, additionalKeywords):
    # rakeKeywords =RAKE.get_RAKE(article)
    # print('rakeKeywords : ',rakeKeywords)
    #print('textRankKeywords : ',textRankKeywords)
    # rakeNltkKeywords = RAKE_NLTK.get_RAKE_nlt(article)
    # print('rakeNltkKeywords : ',rakeNltkKeywords)
    # print('article')
    # print(article)
    textRankKeywords = TextRank.get_TextRank(article, 10)
    # print('TextRank: ')
    # print(textRankKeywords)
    # k_y2 = YAKE.get_keywords(article, 2, 10)
    # print('YAKEn2: ')
    # print(k_y2)
    k_y4 = YAKE.get_keywords(article, 3, 20)
    # print('YAKEn3: ')
    # print(k_y4)
    rake= get_RAKE(article)
    # print('Rake')
    # print(rake)
    pageKeywords = additionalKeywords
    addUnique(pageKeywords, k_y4)
    addUnique(pageKeywords, textRankKeywords)
    addUnique(pageKeywords, rake)
    # print('all')
    # print(pageKeywords)

    return pageKeywords

if __name__ == '__main__':
    text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, Strict inequations, and Nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types systems and systems of mixed types."
    k = get_PageKewords(text)
    print('total k : ',k)