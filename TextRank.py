import spacy
import pytextrank

def get_TextRank(article):
    nlp = spacy.load("en_core_web_sm")

    # add PyTextRank to the spaCy pipeline
    tr = pytextrank.TextRank()
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

    doc = nlp(article)

    # examine the top-ranked phrases in the document
    topKeywords = []

    for i in range(10):
        # print(type(doc._.phrases[i].text))
        # print(type(str(doc._.phrases[i].text)))
        topKeywords.append(doc._.phrases[i].text)
    '''
    for p in doc._.phrases:
        #print("{:.4f} {:5d}  {}".format(p.rank, p.count, p.text))
        print(type(p.text))
    print('***********')
    '''
    # print(topKeywords)
    # print(type(topKeywords))
    # print(type(topKeywords[0]))
    return topKeywords

if __name__ == '__main__':
    text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, Strict inequations, and Nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types systems and systems of mixed types."
    get_TextRank(text)