from flask import Flask, render_template, request
from ScrapArticle import *
import Keywords_Search
import Competitor_Main

app = Flask(__name__, template_folder='templates', static_folder='static')


# 1
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/homepage.html", methods=['POST', 'GET'])
def home():
    return render_template('homepage.html')

@app.route("/keywords.html", methods=['POST', 'GET'])
def findKeywords():
    if request.method == 'POST':
        result = request.form
        url = result['URL']
        keywords = Keywords_Search.findKeywords(url)
        return render_template('keywords.html', result=keywords)
    return render_template('keywords.html')


@app.route("/competitors.html", methods=['POST', 'GET'])
def findCompetitors():
    if request.method == 'POST':
        result = request.form
        url = result['URL']
        title, article, k_1 = scrap(url)
        competitors = Competitor_Main.get_comps(url, title, article)
        return render_template('competitors.html', result=competitors)
    return render_template('competitors.html')


if __name__ == '__main__':
    app.run(debug=True)
