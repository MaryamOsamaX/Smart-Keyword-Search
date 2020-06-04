from newspaper import Article
import YAKE


def scrap(url):
    toi_article = Article(url, language="en")

    # To download the article
    toi_article.download()
    ''''''
    # To parse the article
    toi_article.parse()

    # To perform natural language processing ie..nlp
    toi_article.nlp()

    return toi_article.title, toi_article.text, toi_article.keywords


if __name__ == '__main__':
    url = 'https://towardsdatascience.com/textrank-for-keyword-extraction-by-python-c0bae21bcec0'
    # 'https://cognitev.com/' keywords are bad and need to scroll down
    # 'https://www.foodnetwork.com/recipes/packages/comfort-foods/easy-comfort-food-recipes/easy-comfort-food-recipes' nice
    # 'https://www.allrecipes.com/recipe/242352/greek-lemon-chicken-and-potatoes/?internalSource=staff%20pick&referringId=17562&referringContentType=Recipe%20Hub' it takes the reviews section not the content
    # 'https://www.allrecipes.com/recipes/17562/dinner/' bad
    # 'http://text-analytics101.rxnlp.com/2014/10/all-about-stop-words-for-text-mining.html' good
    # 'https://towardsdatascience.com/textrank-for-keyword-extraction-by-python-c0bae21bcec0' scrap was good but keywords are not

    # # To extract title
    # print("Article's Title:")
    # print(toi_article.title)
    # print("n")
    #
    # # To extract text
    # print("Article's Text:")
    # print(toi_article.text)
    # print("n")
    #
    # # To extract summary
    # print("Article's Summary:")
    # print(toi_article.summary)
    # print("n")
    #
    # # To extract keywords
    # print("Article's Keywords:")
    # print(toi_article.keywords)
    #
    # print('YAKE keywords : ')
    # l = YAKE.get_k(toi_article.text)
    #
    # for i in l:
    #     print(i)

