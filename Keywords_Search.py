from multiprocessing import Pool
import functools

import ScrapArticle
from GoogleSuggestion import getGoogleSuggestion
from KeywordRelevance import calcRelevance
from Keywords import PageKeywords
from Semantics.Semantics import getSemanticForAllKeyWords
from Competitor_Main import get_comps_keywords
from BingAds.data import *


def getKeywords_Original_Semantics(article, keywords1):
    keywords = []  # list of dic
    # keywords['text'] = []
    # keywords['source'] = []
    articleKeywords = PageKeywords.get_PageKewords(article, keywords1)

    f_google = functools.partial(getGoogleSuggestion, articleKeywords)
    f_semantics = functools.partial(getSemanticForAllKeyWords,articleKeywords, article)
    #SemanticsKeywords = getSemanticForAllKeyWords(articleKeywords, article)
    with Pool() as pool:
        res = pool.map(smap, [f_google, f_semantics])

    googleSuggestionKeywords = res[0]
    SemanticsKeywords = res[1]

    for k in articleKeywords:
        keyword = {}
        keyword['text'] = k
        keyword['source'] = 'original'
        keywords.append(keyword)

    keywords.extend(googleSuggestionKeywords)

    for i in SemanticsKeywords:
        for k in i:
            if k not in articleKeywords:
                keyword = {}
                keyword['text'] = k
                keyword['source'] = 'semantics'
                keywords.append(keyword)

    return keywords


def smap(f):
    return f()


def searchForKeywords(url):
    title, article, keywords1 = ScrapArticle.scrap(url)

    f_kos = functools.partial(getKeywords_Original_Semantics, article, keywords1)
    f_kc = functools.partial(get_comps_keywords, url, title)
    f_sk = functools.partial(getKeywordsByURL, url, 10)
    with Pool() as pool:
        res = pool.map(smap, [f_kos, f_kc, f_sk])

    keywords = res[0]
    comps_keywords = res[1]
    suggested_keywords = res[2]
    keyname =[n['text'] for n in keywords]
    for k in comps_keywords:
        if k not in keyname:
            keyword = {}
            keyword['text'] = k
            keyword['source'] = 'competitors'
            keywords.append(keyword)
            keyname.append(k)

    for k in suggested_keywords:
        if k not in keyname:
            keyword = {}
            keyword['text'] = k
            keyword['source'] = 'suggested'
            keywords.append(keyword)

    return keywords, article  # List of dic {'text','source'}


def findKeywords(url):
    keywords, article = searchForKeywords(url)
    keywords_text = [sub['text'] for sub in keywords]
    keywordsWithData = getKeywordData(keywords_text, url)
    kd_text = [sub['text'] for sub in keywordsWithData]
    relevance = calcRelevance(article, keywords_text)
    for i in range(len(keywords_text)):
        j = kd_text.index(keywords_text[i])
        keywordsWithData[j]['source'] = keywords[i]['source']
        keywordsWithData[j]['relevance'] = relevance[i]
    return keywordsWithData

# if __name__ == '__main__':
#     url = 'https://towardsdatascience.com/textrank-for-keyword-extraction-by-python-c0bae21bcec0'
#     keywords, article = searchForKeywords(url)
#     keywords_text = [sub['text'] for sub in keywords]
#     keywordsWithData = getKeywordData(keywords_text, url)
#     kd_text = [sub['text'] for sub in keywordsWithData]
#     relevance = calcRelevance(article, keywords_text)
#     for i in range(len(keywords_text)):
#         j = kd_text.index(keywords_text[i])
#         keywordsWithData[j]['source'] = keywords[i]['source']
#         keywordsWithData[j]['relevance'] = relevance[i]
#     print(keywordsWithData)
#     # print(keywords['text'])
