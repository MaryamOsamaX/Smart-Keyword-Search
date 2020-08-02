from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
import numpy as np
import numpy.linalg as LA
# import PageKeywords
# import ScrapArticle
# import time


def cx(a, b):
    if LA.norm(a) * LA.norm(b) != 0:
        return round(np.inner(a, b) / (LA.norm(a) * LA.norm(b)), 3)
    else:
        return 0.0


def calcRelevance(article, keywords):
    articleList = [article]
    stopWords = stopwords.words('english')

    vectorizer = CountVectorizer(stop_words=stopWords)

    trainVectorizerArray = vectorizer.fit_transform(articleList).toarray()
    testVectorizerArray = vectorizer.transform(keywords).toarray()
    # cx = lambda a, b : (round(np.inner(a, b)/(LA.norm(a)*LA.norm(b)), 3)) if((LA.norm(a)*LA.norm(b) != 0) else 0

    #i = 0
    relevance = []
    for testV in testVectorizerArray:
        cosine = cx(trainVectorizerArray[0], testV)
        #print(keywords[i], " = ", cosine)
        relevance.append(cosine)
        #i += 1

    return relevance


# transformer.fit(trainVectorizerArray)
# print()
# print (transformer.transform(trainVectorizerArray).toarray())
#
# transformer.fit(testVectorizerArray)
# print()
# tfidf = transformer.transform(testVectorizerArray)
# print (tfidf.todense())
# if __name__ == '__main__':
#
    # url = 'https://towardsdatascience.com/textrank-for-keyword-extraction-by-python-c0bae21bcec0'
    # start_time = time.time()
    # title, article, keywords1 = ScrapArticle.scrap(url)
    # articleKeywords = PageKeywords.get_PageKewords(article, keywords1)
    # r = calcRelevance(article, articleKeywords)
    # for i in range(len(r)):
    #     print(articleKeywords[i], ' = ', r[i])
    # print("--- %s seconds ---" % (time.time() - start_time))
    # s={}
    # s['ss']=[0,1,0,2,3]
    # s['ss'] =r
    # print(s['ss'])