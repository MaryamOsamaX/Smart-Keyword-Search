from multi_rake import Rake
from selenium import webdriver
from urllib.request import urlopen
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

article = ''
url = "https://cognitev.com/"
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
'''
try:
    page = urlopen(link)
except:
    print("Error opening the URL in this -> ", link)
'''
soup = BeautifulSoup(driver.page_source, 'html.parser')
# + soup.find_all('ul') + soup.find_all('li')
titles = soup.find_all('title')
h1 = soup.find_all('h1')
h2 = soup.find_all('h2')
h3 = soup.find_all('h3')
h4 = soup.find_all('h4')
h5 = soup.find_all('h5')
h6 = soup.find_all('h6')
p = soup.find_all('p')
span = soup.find_all('span')
a = soup.find_all('a')

print('titles_______________________________')
for i in titles:
    print(i.text)

print('h1_______________________________')
for i in h1:
    print(i.text)

print('h2_______________________________')
for i in h2:
    print(i.text)

print('p_______________________________')
for i in p:
    print(i.text)

print('span_______________________________')
for i in span:
    print(i.text)

print('a_______________________________')
for i in a:
    print(i.text)


