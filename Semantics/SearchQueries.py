#!pip install pytrends==4.7.3

from pytrends.request import TrendReq
def getSearchQueries(searchWord):
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = [searchWord]
    pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    df=pytrends.related_queries()
    et=pytrends.suggestions(searchWord)
    print(et)
    print(df)
    
'''
queries=[]
if df[sen]['top'] is not None:
    for r in df[sen]['top']['query']:
         queries.append(r)
else:
    print('none')
    
if df[sen]['rising'] is not None:
    for r in df[sen]['rising']['query']:
         queries.append(r) 
         print(r)
else:
    print('none')
    
print(queries)
'''

#https://pypi.org/project/pytrends/4.7.3/#description
#https://stackoverflow.com/questions/8936610/how-can-i-create-every-combination-possible-for-the-contents-of-two-arrays