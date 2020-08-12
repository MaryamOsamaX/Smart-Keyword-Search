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
from ScrapArticle import *
import sys

'''
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

    #check the list
    competitors = get_distict_comps(competitors)
    
    # 2- get traffic reach
    for comp in competitors:
        comp.traffic_reach = getWebPageReach(comp.url)

    #sort competitors based on traffic_reach descending
    #from largest to smallest
    competitors.sort(reverse=True, key= sort_based_on_traffic_reach)

    # 3- get similarity
    for comp in competitors:
        comp.similarity = getSimilarity(url, comp.text)

    # 4- get keywords
    count = 0
    for comp in competitors:
        comp.keywords = get_comp_keywords(comp.url)
        count += 1
        print(count)
        if(count >= 10):
            break

    return competitors
'''
def sort_based_on_traffic_reach(elem):
    return elem.traffic_reach


def get_comp_keywords(url):#till finish all
    # urls = getURLs(url, title)
    keywords = []
    keywords = getKeywordsByURL(url)
    # for l in urls:
    #     keywords.extend(getKeywordsofCompetitor(l))

    return keywords

def get_comps_keywords(url, title):  # till finish all
    urls = getURLs(url, title)
    keywords = []
    if len(urls) >= 10:
        for i in range(10):
            keywords.extend(getKeywordsByURL(urls[i]))
    else:
        for i in range(len(urls)):
            keywords.extend(getKeywordsByURL(urls[i]))
    return keywords


def get_comps(url, title, article): #Should we add title???
    competitors = []
    urls = getURLs(url, title)
    for i in range(len(urls)):
        s = Competitor()
        s.url = urls[i]
        competitors.append(s)

    #check the list
    competitors = get_distict_comps(competitors)
    
    # 2- get traffic reach
    for comp in competitors:
        comp.traffic_reach = getWebPageReach(comp.url)

    # 3- get similarity
    for comp in competitors:
        comp.similarity = getSimilarity(article, comp.text)

    comps = []
    for comp in competitors:
        c = {}
        c['url'] = comp.url
        c['reach'] = comp.traffic_reach
        c['similarity'] = comp.similarity
        comps.append(c)
    cs =sorted(comps, key=lambda i: i['reach'], reverse=True)
    return cs

def get_distict_comps(comps):
    for comp in comps:
        comp.text = scrap(comp.url)
        
    #list of pages that appears twice in the comp
    matches = []
    for i in range (len(comps)):
        for j in range(i+1, len(comps)):
            if (comps[i].text == comps[j].text):
                matches.append(comps[j])
            
    for match in matches:
        comps.remove(match)
    return comps

if __name__ == '__main__':
    # #########################################################
    # url = "https://blog.hubspot.com/marketing/what-is-digital-marketing"
    # title = "what is digital marketing"
    # #########################################################
    #
    # # get related comps
    # results = get_all_comps(url, title)
    url = 'https://www.autoexpress.co.uk/best-cars/103133/best-new-cars-for-2020'
    title, article, k_1 = scrap(url)
    competitors = get_comps(url, title, article)
    print('len = ',len(competitors))
    print(competitors)
    original_stdout = sys.stdout
    with open('competitors.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print(competitors)
        sys.stdout = original_stdout
