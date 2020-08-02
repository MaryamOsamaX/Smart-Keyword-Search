import yake


def get_keywords(text, n, x):
    language = "en"
    max_ngram_size = n
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = x
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold,
                                                dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords,
                                                features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    k = []
    for kw in keywords:
        k.append(kw[0])
    return k


if __name__ == '__main__':
    text = '''
    Top highlight Understand TextRank for Keyword Extraction by Python A scratch implementation by Python and spaCy to help you
     understand PageRank and TextRank for Keyword Extraction. Xu LIANG Follow Feb 18, 2019   ·   7  min read image from www.adaringadventure.com
     Introduction TextRank is an algorithm based on PageRank, which often used in keyword extraction and text summarization.
     In this article, I will help you understand how TextRank works with a keyword extraction example and show the implementation by Python.
     Keywords Extraction with TextRank, NER, etc Table of Contents Understand PageRank Implementation of PageRank Keyword Extraction by TextRank
     Implementation of Keyword Extraction Understand PageRank There are tons of articles talking about PageRank, so I just give a brief introduction to PageRank.
     This will help us understand TextRank later because it is based on PageRank. PageRank (PR) is an algorithm used to calculate the weight for web pages.
     We can take all web pages as a big directed graph. In this graph, a node is a webpage. If webpage A has the link to web page B,
     it can be represented as a directed edge from A to B. After we construct the whole graph, we can assign weights for web pages by the following formula.
      Here is an example to better understand the notation above. We have a graph to represent how web pages link to each other. Each node represents a webpage,
      and the arrows represent edges. We want to get the weight of webpage  e .
      We can rewrite the summation part in the above function to a simpler version.
      We can get the weight of webpage  e  by the following function. We can see the weight of the webpage  e  is dependent on the weights of its inbound pages. We need to run this iteration much time to get the final weight.
      In the initialization,the importance of each webpage is 1. Implementation of PageRank We can use a matrix to represent the inbound and outbound links among a, b, e, f in the graph. Each node in a row means the inbound links from other nodes.
       For example, for the  e  row, node  a  and  b  have outbound links to node  e . This presentation will simplify the calculation for updating the weight.
        According to the  1/|Out(Vi)|  from the function, we should normalize each column. We use this matrix to multiply with the weight of all nodes.
        This is just one iteration without dumping factor  d . We can use Python to iterate many times. import numpy as np g = [[0, 0, 0, 0],      [0, 0, 0, 0],      [1, 0.5, 0, 0],      [0, 0.5, 0, 0]] g = np.array(g) pr = np.array([1, 1, 1, 1]) # initialization for a, b, e, f is 1 d = 0.85 for iter in range(10):     pr = 0.15 + 0.85 * np.dot(g, pr)     print(iter)     print(pr) Output 0 [0.15  0.15  1.425 0.575] 1 [0.15    0.15    0.34125 0.21375] 2 [0.15    0.15    0.34125 0.21375] 3 [0.15    0.15    0.34125 0.21375] 4 [0.15    0.15    0.34125 0.21375] 5 [0.15    0.15    0.34125 0.21375] 6 [0.15    0.15    0.34125 0.21375] 7 [0.15    0.15    0.34125 0.21375] 8 [0.15    0.15    0.34125 0.21375] 9 [0.15    0.15    0.34125 0.21375] 10 [0.15    0.15    0.34125 0.21375] So the weight (PageRank value) of e is 0.34125. If we change the directed edge as the undirected edge, we can change the matrix correspondingly. Normalize it. We should change the code correspondingly. import numpy as np g = [[0, 0, 0.5, 0],      [0, 0, 0.5, 1],      [1, 0.5, 0, 0],      [0, 0.5, 0, 0]] g = np.array(g) pr = np.array([1, 1, 1, 1]) # initialization for a, b, e, f is 1 d = 0.85 for iter in range(10):     pr = 0.15 + 0.85 * np.dot(g, pr)     print(iter)     print(pr) Output 0 [0.575 1.425 1.425 0.575] 1 [0.755625 1.244375 1.244375 0.755625] 2 [0.67885937 1.32114062 1.32114062 0.67885937] 3 [0.71148477 1.28851523 1.28851523 0.71148477] 4 [0.69761897 1.30238103 1.30238103 0.69761897] 5 [0.70351194 1.29648806 1.29648806 0.70351194] 6 [0.70100743 1.29899257 1.29899257 0.70100743] 7 [0.70207184 1.29792816 1.29792816 0.70207184] 8 [0.70161947 1.29838053 1.29838053 0.70161947] 9 [0.70181173 1.29818827 1.29818827 0.70181173] So the weight (PageRank value) of e is 1.29818827. Keyword Extraction by TextRank What the difference between TextRank and PageTank? The simple answer is PageRank is for webpage ranking, and TextRank is for text ranking. The webpage in PageRank is the text in TextRank, so the basic idea is the same. Here we have some text, taken from  here . I will use spaCy We split a document  into  several sentences, and we only store those words with specific POS tags. We use spaCy for POS tagging. import spacy nlp = spacy.load('en_core_web_sm') content = 'The Wandering Earth, described as China’s first big-budget science fiction thriller, quietly made it onto screens at AMC theaters in North America this weekend, and it shows a new side of Chinese filmmaking — one focused toward futuristic spectacles rather than China’s traditionally grand, massive historical epics. At the same time, The Wandering Earth feels like a throwback to a few familiar eras of American filmmaking. While the film’s cast, setting, and tone are all Chinese, longtime science fiction fans are going to see a lot on the screen that reminds them of other movies, for better or worse. ' doc = nlp(content) for sents in doc.sents:     print(sents.text) We split the paragraph into three sentences. The Wandering Earth, described as China’s first big-budget science fiction thriller, quietly made it onto screens at AMC theaters in North America this weekend, and it shows a new side of Chinese filmmaking — one focused toward futuristic spectacles rather than China’s traditionally grand, massive historical epics. At the same time, The Wandering Earth feels like a throwback to a few familiar eras of American filmmaking. While the film’s cast, setting, and tone are all Chinese, longtime science fiction fans are going to see a lot on the screen that reminds them of other movies, for better or worse. Because most of the words in a sentence are not useful to determine the importance, we only consider the words with NOUN, PROPN, VERB POS tags. This is optional, you can also use all words. candidate_pos = ['NOUN', 'PROPN', 'VERB'] sentences = [] ​ for sent in doc.sents:     selected_words = []     for token in sent:         if token.pos_ in candidate_pos and token.is_stop is False:             selected_words.append(token)     sentences.append(selected_words) ​ print(sentences) Output [[Wandering, Earth, described, China, budget, science, fiction, thriller, screens, AMC, theaters, North, America, weekend, shows, filmmaking, focused, spectacles, China, epics], [time, Wandering, Earth, feels, throwback, eras, filmmaking], [film, cast, setting, tone, science, fiction, fans, going, lot, screen, reminds, movies]] Each word is a  node  in PageRank. We set the window size as k. [w1, w2, …, w_k], [w2, w3, …, w_{k+1}], [w3, w4, …, w_{k+2}] are windows. Any two-word pairs in a window are considered have an undirected edge. We take  [time, Wandering, Earth, feels, throwback, eras, filmmaking]  as the example, and set the window size k=4, so we get 4 windows,  [time, Wandering, Earth, feels] ,  [Wandering, Earth, feels, throwback] ,  [Earth, feels, throwback, eras] ,  [feels, throwback, eras, filmmaking] . For window  [time, Wandering, Earth, feels] , any two words pair has an undirected edge. So we get  (time, Wandering), (time, Earth), (time, feels), (Wandering, Earth), (Wandering, feels), (Earth, feels) . Based on this graph, we can calculate the weight for each node(word). The most important words can be used as keywords. Implementation of Keyword Extraction Here I implement a complete example by Python, and we use spaCy to get the POS tag of words. This  TextRank4Keyword  implements all functions I described in the last section. We can see the output of one paragraph. text = ' The Wandering Earth, described as China’s first big-budget science fiction thriller, quietly made it onto screens at AMC theaters in North America this weekend, and it shows a new side of Chinese filmmaking — one focused toward futuristic spectacles rather than China’s traditionally grand, massive historical epics. At the same time, The Wandering Earth feels like a throwback to a few familiar eras of American filmmaking. While the film’s cast, setting, and tone are all Chinese, longtime science fiction fans are going to see a lot on the screen that reminds them of other movies, for better or worse. ' ​ tr4w = TextRank4Keyword() tr4w.analyze(text, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False) tr4w.get_keywords(10) Output science - 1.717603106506989 fiction - 1.6952610926181002 filmmaking - 1.4388798751402918 China - 1.4259793786986021 Earth - 1.3088154732297723 tone - 1.1145002295684114 Chinese - 1.0996896235078055 Wandering - 1.0071059904601571 weekend - 1.002449354657688 America - 0.9976329264870932 budget - 0.9857269586649321 North - 0.9711240881032547 Check out my other posts on  Medium , with a better  TOC list view ! GitHub:  https://github.com/BrambleXu LinkedIn:  www.linkedin.com/in/xu-liang Blog:  https://bramblexu.org News Graph I also implement TextRank for extracting keywords from news and visualize it. Welcome to check it. BrambleXu/news-graph Key information extraction from text and graph visualization - BrambleXu/news-graph github.com Demo of News Graph '''

    print(get_k(text))