from multi_rake import Rake
def get_RAKE(article):
    rake = Rake()
    keywords = rake.apply(article)
    topKeywords = []

    for i in range(10):
        topKeywords.append(keywords[i][0])
    #print(topKeywords)
    return topKeywords

if __name__ == '__main__':
    text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, Strict inequations, and Nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types systems and systems of mixed types."
    get_RAKE(text)