# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 23:03:15 2020

@author: Kaneki Kiddo
"""
import re
from GoogleAPI import getComps


#########################################################
url = "https://blog.hubspot.com/marketing/what-is-digital-marketing"
title = "what is digital marketing"
#########################################################

#get related comps
results = getComps(url, title)
print(len(results))