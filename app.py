from flask import Flask

from flask import Flask, render_template, url_for, request
import requests
import json
import ScrapPage
import PageKeywords
app = Flask(__name__,template_folder='templates', static_folder='static')


#1
@app.route('/')
def hello_world():
    return render_template('Home.html')

@app.route("/keywords/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        result = request.form
        url =result['URL']
        k = result['kList']
        c = result['cList']
        # print(url,' ',k,' ',c)
        article = ScrapPage.scrap_Page(url)
        pageKeywords = PageKeywords.get_PageKewords(article)
        return render_template('keywords.html', result=pageKeywords)
    return render_template('keywords.html')

if __name__ == '__main__':
    app.run()
