import requests
from bs4 import BeautifulSoup


def getGoogleSuggestion(keywords):
    suggestedKeywords = []
    for i in keywords:
        r = requests.get('http://suggestqueries.google.com/complete/search?output=toolbar&hl=ru&q={}&gl=in&q=' + i)
        soup = BeautifulSoup(r.content, 'lxml')
        suggestions = soup.find_all('suggestion')
        # suggestions_list=[]
        for suggestion in suggestions:
            # suggestions_list.append(suggestion.attrs['data'])
            if suggestion.attrs['data'] not in keywords:
                keyword = {}
                keyword['text'] = suggestion.attrs['data']
                keyword['source'] = 'suggested'
                suggestedKeywords.append(keyword)

    return suggestedKeywords
