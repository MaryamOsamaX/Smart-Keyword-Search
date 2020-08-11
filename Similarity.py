# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 19:19:01 2020

@author: Kaneki Kiddo
"""

from ScrapArticle import scrap
from rouge import Rouge


def getSimilarity(txt_1, txt_2):
    rouge = Rouge()
    scores = rouge.get_scores(txt_1, txt_2)

    '''
    our main concern is the value of rouge-l which stands for the Longest Common 
    Subsequence takes into account sentence level structure similarity naturally and
    identifies longest co-occurring in sequence n-grams automatically.
    
    then the value of f is our goal as it's the f measure the harmonic mean of 
    precision and recall
    f = 2 * (recall + precision) / (recall * precision)
    '''
    return scores[0]['rouge-l']['f']
