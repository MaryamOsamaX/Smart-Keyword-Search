# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 23:03:15 2020

@author: Kaneki Kiddo
"""
from Competitors.GoogleAPI import getURLs
from BingAds.data import getKeywordsByURL
from Competitors.Competitor import Competitor
from Competitors.CompTraffic import getWebPageReach
from Similarity import getSimilarity


def get_all_comps(url, title):
    '''
    this function does the following:
    ---------------------------------
        1- get urls of comps
        2- get traffic reach
        3- get similarity
        4- get keywords
        
        #in the end... return list of distinct ordered by traffic comps
    '''
    competitors = []
    # 1- get urls
    urls = []
    urls = getURLs(url, title)
    for i in range(len(urls)):
        s = Competitor()
        s.url = urls[i]
        competitors.append(s)

    # 2- get traffic reach
    for comp in competitors:
        comp.traffic_reach = getWebPageReach(comp.url)

    #sort competitors based on traffic_reach descending
    #from largest to smallest
    competitors.sort(reverse=True, key= sort_based_on_traffic_reach)

    # 3- get similarity
    for comp in competitors:
        comp.similarity = getSimilarity(url, comp.url)

    # 4- get keywords
    count = 0
    for comp in competitors:
        comp.keywords = get_comp_keywords(comp.url)
        count += 1
        print(count)
        if(count >= 10):
            break

    return competitors

def sort_based_on_traffic_reach(elem):
    return elem.traffic_reach


def get_comp_keywords(url):#till finish all
    # urls = getURLs(url, title)
    keywords = []
    keywords = getKeywordsByURL(url)
    # for l in urls:
    #     keywords.extend(getKeywordsofCompetitor(l))

    return keywords


def get_comps(url, title, article): #Should we add title???
    competitors = []
    urls = getURLs(url, title)
    for i in range(len(urls)):
        s = Competitor()
        s.url = urls[i]
        competitors.append(s)

    # 2- get traffic reach
    for comp in competitors:
        comp.traffic_reach = getWebPageReach(comp.url)

    # 3- get similarity
    for comp in competitors:
        comp.similarity = getSimilarity(article, comp.url)

    return competitors


if __name__ == '__main__':
    #########################################################
    url = "https://blog.hubspot.com/marketing/what-is-digital-marketing"
    title = "what is digital marketing"
    #########################################################

    # get related comps
    results = get_all_comps(url, title)
