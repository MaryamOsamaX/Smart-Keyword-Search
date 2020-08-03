from multiprocessing import Pool
import functools
import re
import ScrapArticle
from KeywordRelevance import calcRelevance
from Keywords import PageKeywords
from Semantics.Semantics import getSemanticForAllKeyWords
from Competitor_Main import get_comps_keywords
from BingAds.data import *


def getKeywords_Original_Semantics(article, keywords1):
    keywords = []  # list of dic
    # keywords['text'] = []
    # keywords['source'] = []
    articleKeywords = clearKeywords(PageKeywords.get_PageKewords(article, keywords1))
    SemanticsKeywords = getSemanticForAllKeyWords(articleKeywords, article)
    #SemanticsKeywords = []
    for k in articleKeywords:
        keyword = {}
        keyword['text'] = k
        keyword['source'] = 'original'
        keywords.append(keyword)

    for i in SemanticsKeywords:
        i = clearKeywords(i)
        for k in i:
            if k not in articleKeywords:
                keyword = {}
                keyword['text'] = k
                keyword['source'] = 'semantics'
                keywords.append(keyword)

    return keywords


def smap(f):
    return f()

def clearKeywords(pageKeywords):
    for i,item in enumerate(pageKeywords):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, item)
        if url:
            pageKeywords.remove(item)
            continue
        if item.isnumeric():
            pageKeywords.remove(item)
            continue
            #print('remove ', item)
        pageKeywords[i] = re.sub(r'[^\w\s-]', '', pageKeywords[i])
        pageKeywords[i] = pageKeywords[i].lower()

        #print(pageKeywords[i])
    return pageKeywords

def searchForKeywords(url):
    title, article, keywords1 = ScrapArticle.scrap(url)

    # f_kos = functools.partial(getKeywords_Original_Semantics, article, keywords1)
    # f_kc = functools.partial(get_comps_keywords, url, title)
    # f_sk = functools.partial(getKeywordsByURL, url, 10)
    # with Pool() as pool:
    #     res = pool.map(smap, [f_kos, f_kc, f_sk])

    # keywords = res[0]
    # comps_keywords = res[1]
    # suggested_keywords = res[2]
    keywords = getKeywords_Original_Semantics(article, keywords1)

    comps_keywords = clearKeywords(get_comps_keywords(url, title))
    suggested_keywords = clearKeywords(getKeywordsByURL(url, 10))
    for k in comps_keywords:
        if k not in keywords:
            keyword = {}
            keyword['text'] = k
            keyword['source'] = 'competitors'
            keywords.append(keyword)
    for k in suggested_keywords:
        if k not in keywords:
            keyword = {}
            keyword['text'] = k
            keyword['source'] = 'suggested'
            keywords.append(keyword)

    return keywords, article  # List of dic {'text','source'}


def findKeywords(url):
    keywords, article = searchForKeywords(url)
    keywords_text = [sub['text'] for sub in keywords]
    #keywords_text.extend(['novo', 'matrix'])
    keywordsWithData = getKeywordData(keywords_text, url)
    kd_text = [sub['text'] for sub in keywordsWithData]
    relevance = calcRelevance(article, keywords_text)
    # print('keywords_text ',len(keywords_text))
    # print(keywords_text)
    # print('kd_text', len(kd_text))
    # print(kd_text)
    # print('all data ',len(keywordsWithData))
    # for i in keywordsWithData:
    #     print(i)
    for i in range(len(keywords_text)):
        if keywords_text[i] in kd_text:
            j = kd_text.index(keywords_text[i])
            keywordsWithData[j]['source'] = keywords[i]['source']
            keywordsWithData[j]['relevance'] = relevance[i]
    return keywordsWithData


if __name__ == '__main__':
    url='https://www.autoexpress.co.uk/best-cars/103133/best-new-cars-for-2020'
    ks =findKeywords(url)
    for k in ks:
        print(k['text'],' ',k['source'])
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
