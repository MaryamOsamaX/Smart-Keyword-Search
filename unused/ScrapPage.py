from selenium import webdriver
from urllib.request import urlopen
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup, Comment
import chromedriver_binary
import codecs
import re

def scrap_Page(url):
    #sroll down page part : start
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    try:
        iframe = driver.find_element_by_id("nvpush_popup_background_iframe")
        cross = driver.find_element_by_id("nvpush_cross")
        cross.click()
    except:
        pass

    while True:
        try:
            loadmore = driver.find_element_by_id("bottomPager")
            loadmore.click()
        except:
            print("Reached bottom of page")
            break
    # sroll down page part : end

    #Start page scrapping
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    blacklist = [
        'style',
        'script',
        'header',
        'Comment'
    ]
    #remove all blacklist tags
    for n in blacklist:
        for tag in soup.find_all(n):
            tag.replaceWith('')
    # remove all comments
    for comments in soup.findAll(text=lambda text: isinstance(text, Comment)):
        comments.extract()
    article = ''
    if soup.find_all('article'):
        print('in article ')
        for article_1 in soup.find_all('article'):
            #print(article_1.find_all(text=True))
            for i in article_1.find_all(text=True):
                article += i + ' '
        #print(article)
    else:
        print('there is no article tag')
        soupp = soup.find_all('div')
        text_div = []
        # print(soupp)
        # print('---------------------')
        for s in soupp:
            #print(s)
            for i in s.find_all(text=True):
                if i not in text_div:
                    text_div.append(i)
        for i in text_div:
            article+=i +' '

    article = article.replace('\n', ' ')
    while '  ' in article:
        article = article.replace('  ', ' ')

    #print(article)
    return soup.find('title').text,article,[]
        # print(article)
        # f = codecs.open("demo.txt", "w", "utf-8")
        # f.write(article)
        # f.close()
        #
        # for s in soupp:
        #     text_elements = [t for t in s.find_all(text=True)]  # if t.parent.name not in blacklist
        #     if text_elements and text_elements not in text_div:
        #         text_div.append(text_elements)
        #         for stmt in text_elements:
        #             print('stmt type = ',type(str(stmt)))
        #             article+= str(stmt)+' '
        #     print('**', text_elements)
        #
        #     article += str(text_elements)+' '
        # print(text_div)
        # print('*****************************')
        # print(article)
        # f = codecs.open("demo.txt", "w", "utf-8")
        # f.write(article)
        # f.close()
        # print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')

    '''
        final_paragraphs = []
        for s in text_div:
            ss = ''
            if s:
                for words in s:
                    ss += ' ' + words
                ss = ss.replace('\n', '')
                # ss = ss.replace('  ', '')
                while '  ' in ss:
                    ss = ss.replace('  ', ' ')
                if ss and not ss.isspace():
                    final_paragraphs.append(ss)
                    print(ss)
                    print('********************************************************')
        print(len(final_paragraphs))
        '''


if __name__ == '__main__':
    print(scrap_Page('https://www.autoexpress.co.uk/best-cars/103133/best-new-cars-for-2020'))