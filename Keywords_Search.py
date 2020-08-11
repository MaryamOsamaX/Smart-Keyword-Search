from multiprocessing import Pool
import functools
import re
import ScrapArticle
from KeywordRelevance import calcRelevance
from Keywords import PageKeywords
from Semantics.Semantics import getSemanticForAllKeyWords
from Competitor_Main import get_comps_keywords
from BingAds.data import *
import time


def getKeywords_Original_Semantics(article, keywords1):
    keywords = []  # list of dic
    # keywords['text'] = []
    # keywords['source'] = []
    s = time.time()
    articleKeywords = list(set(clearKeywords(PageKeywords.get_PageKewords(article, keywords1))))
    print('fin original  ', time.time() - s)
    s = time.time()
    SemanticsKeywords = getSemanticForAllKeyWords(articleKeywords, article)
    print('fin semantics  ', time.time() - s)
    # SemanticsKeywords = []
    textonly=[]
    for k in articleKeywords:
        keyword = {}
        keyword['text'] = k
        keyword['source'] = 'original'
        keywords.append(keyword)
        textonly.append(str(k))

    for i in SemanticsKeywords:
        i = clearKeywords(i)
        for k in i:
            if k not in articleKeywords:
                keyword = {}
                keyword['text'] = k
                keyword['source'] = 'semantics'
                keywords.append(keyword)
                textonly.append(str(k))

    return keywords, list(set(textonly))


def smap(f):
    return f()


def clearKeywords(pageKeywords):
    for i, item in enumerate(pageKeywords):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, item)
        if url:
            pageKeywords.remove(item)
            continue
        if item.isnumeric():
            pageKeywords.remove(item)
            continue
            # print('remove ', item)
        pageKeywords[i] = re.sub(r'[^\w\s-]', '', pageKeywords[i])
        pageKeywords[i] = pageKeywords[i].lower()

        # print(pageKeywords[i])
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
    s = time.time()
    keywords, textonly= getKeywords_Original_Semantics(article, keywords1)
    print('fin o & s  ', time.time() - s)
    s = time.time()
    comps_keywords = list(set(clearKeywords(get_comps_keywords(url, title))))
    print('fin comp  ', time.time() - s)
    s = time.time()
    suggested_keywords = list(set(clearKeywords(getKeywordsByURL(url, 10))))
    print('fin suggested  ', time.time() - s)
    for k in comps_keywords:
        if k not in keywords:
            keyword = {}
            keyword['text'] = k
            keyword['source'] = 'competitors'
            keywords.append(keyword)
            textonly.append(str(k))

    for k in suggested_keywords:
        if k not in keywords:
            keyword = {}
            keyword['text'] = k
            keyword['source'] = 'suggested'
            keywords.append(keyword)
            textonly.append(str(k))

    return keywords, article, list(set(textonly))  # List of dic {'text','source'}


def get_keywords_data_50(keywords_text, url):
    keywordsWithData = []
    j = 50
    i = 0
    for x in range(len(keywords_text)):
        if j >= len(keywords_text):
            # print(i,' ',j,'  end  ',keywords_text[i:])
            keywordsWithData.extend(getKeywordData(keywords_text[i:], url))
            break
        else:
            # print(i,' ',j,'  ',keywords_text[i:j])
            keywordsWithData.extend(getKeywordData(keywords_text[i:j], url))
            i += 50
            j += 50

    return keywordsWithData


def findKeywords(url):
    s = time.time()
    keywords, article, keywords_text = searchForKeywords(url)
    print('fin get keywords ', time.time() - s)
    print('total words = ', len(keywords))
    s = time.time()
    # keywords_text = list(set(clearKeywords([str(sub['text']) for sub in keywords])))
    # keywords_text.extend(['novo', 'matrix'])
    keywordsWithData = get_keywords_data_50(keywords_text, url)
    kd_text = list(set(clearKeywords([str(sub['text']) for sub in keywordsWithData])))
    relevance = calcRelevance(article, kd_text)
    # print('keywords_text ',len(keywords_text))
    # print(keywords_text)
    # print('kd_text', len(kd_text))
    # print(kd_text)
    # print('all data ',len(keywordsWithData))
    # for i in keywordsWithData:
    #     print(i)
    print('keywords_text', len(keywords_text))
    print('kd_text', len(kd_text))
    for i in range(len(kd_text)):
        if kd_text[i] in keywords_text:
            j = keywords_text.index(kd_text[i])
            keywordsWithData[i]['source'] = keywords[j]['source']
            keywordsWithData[i]['relevance'] = relevance[i]
            comp = 0.0
            if str(keywordsWithData[i]['competition']) == 'Low' or str(keywordsWithData[i]['competition']) == 'low':
                comp = 0.9
            elif str(keywordsWithData[i]['competition']) == 'Medium' or str(keywordsWithData[i]['competition']) == 'medium':
                comp = 0.6
            elif str(keywordsWithData[i]['competition']) == 'High' or str(keywordsWithData[i]['competition']) == 'high':
                comp = 0.3

            keywordsWithData[i]['rate'] = (0.1 * (keywordsWithData[i]['avgVolume'] + comp
                                                  + keywordsWithData[i]['avgCpc'] + comp)
                                           + 0.2 * (keywordsWithData[i]['relevance'] + keywordsWithData[i]['ctr']
                                                    + keywordsWithData[i]['impressions']+ keywordsWithData[i]['clicks']))

    print('fin data  ', time.time() - s)
    r = sorted(keywordsWithData, key=lambda i: i['rate'], reverse=True)
    res = sorted(r[:100], key=lambda i: i['volume'], reverse=True)
    return res


if __name__ == '__main__':
    url = 'https://www.autoexpress.co.uk/best-cars/103133/best-new-cars-for-2020'
    ss = time.time()
    ks = findKeywords(url)
    original_stdout = sys.stdout
    with open('filename1.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print(ks)
        sys.stdout = original_stdout
    print('fin total  ', time.time() - ss)
    print('total final words = ', len(ks))
    for i, k in enumerate(ks):
        print(i, k['text'], ' ', k['source'])
    # k=[]
    # for i in range(31):
    #     k.append('k'+str(i))
    # get_keywords_data_50(k,'')
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
