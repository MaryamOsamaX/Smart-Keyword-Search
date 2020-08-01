# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 23:03:15 2020

@author: Kaneki Kiddo
"""
from Competitors.GoogleAPI import getURLs
from Competitors.CompetitorsKeywords import getKeywordsofCompetitor
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
        
    #2- get traffic reach
    for comp in competitors:
        comp.traffic_reach = getWebPageReach(comp.url)
    
    #3- get similarity
    for comp in competitors:
        comp.similarity = getSimilarity(url, comp.url)
    
    #4- get keywords
    for comp in competitors:
        comp.keywords = getKeywordsofCompetitor(comp.url)
        
    return competitors



if __name__ == '__main__':
    
    #########################################################
    url = "https://blog.hubspot.com/marketing/what-is-digital-marketing"
    title = "what is digital marketing"
    #########################################################
    
    #get related comps
    results = get_all_comps(url, title)

