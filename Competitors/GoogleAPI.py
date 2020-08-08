# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 23:11:38 2020

@author: Kaneki Kiddo
"""

import requests
import re

API_KEY = "AIzaSyBhyQIfqPwttrNeXUfDHarEMrs_yGWEAoc"
SEARCH_ENGINE_ID = "011076497418570699014:2k5x30zrgsq"

def useGoogleAPI(query, numberOfPages):
    results =[]
    resultNumber = 1
    if(len(query) > 2048):
        print("The query: ", query, " is too long") # greater than 2048 chars
        return results
    for page in range(1, numberOfPages + 1):
        start = (page - 1) * 10 + 1
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
        data = requests.get(url).json()
        # get the result items
        search_items = data.get("items")
        # iterate over 10 results found
        if(search_items == None):
            break
        else:
            for i, search_item in enumerate(search_items, start=1):
                link = search_item.get("link")
                results.append(link)
                resultNumber += 1
    return results



def getURLs(url, title):
    #remember to change values as
    '''
    number_of_related = 2
    number_of_titled = 3
    number_of_sites = 1
    '''  
    number_of_related = 2
    number_of_titled = 3
    number_of_sites = 1
    final_results = []
    sites = []
    
    #print("Loading Related...")
    results_related = useGoogleAPI("related: " + url, number_of_related)
    #print("Done\n" + "Loading Titled...")
    results_titled = useGoogleAPI("intitle: " + title, number_of_titled)
    #print("Done")
    total = results_related + results_titled
    total = list(dict.fromkeys(total))
    
    for item in total:
        str1 = item
        match = re.findall('\\b(/+)\\b', str1)
        if(len(match) == 0):
            sites.append(item)
        else:
            final_results.append(item)
    if(len(final_results) < 50):
        #print("Loading Sites...")
        for site in sites:
            results_sites = useGoogleAPI(title + " site: " + site, number_of_sites)
            for item in results_sites:
                str1 = item
                match = re.findall('\\b(/+)\\b', str1)
                if(len(match) != 0):
                    final_results.append(item)
            
            final_results = list(dict.fromkeys(final_results))
            if(len(final_results) >= 50):
                break
    
    final_results.remove(url)
    return final_results