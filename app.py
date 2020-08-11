from flask import Flask, render_template, request
from ScrapArticle import *
import Keywords_Search
import Competitor_Main

app = Flask(__name__, template_folder='templates', static_folder='static')


# 1
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/homepage", methods=['POST', 'GET'])
def home():
    return render_template('homepage.html')

@app.route("/keywords", methods=['POST', 'GET'])
def findKeywords():
    if request.method == 'POST':
        result = request.form
        url = result['URL']
        #keywords = Keywords_Search.findKeywords(url)
        keywords =[{'text': 'suv', 'competition': 'High', 'volume': 247170, 'avgVolume': 207022, 'relevance': 0.138, 'suggestedBid': 1.95, 'avgCpc': 1.71, 'avgPosition': 1.14, 'clicks': 12965.09, 'ctr': 0.05, 'impressions': 244224.28, 'totalCost': 22136.86, 'rate': 65929.57519999999, 'source': 'semantics'}, {'text': 'go kart', 'competition': 'High', 'volume': 607340, 'avgVolume': 722377, 'relevance': 0.116, 'suggestedBid': 0.28, 'avgCpc': 0.08, 'avgPosition': 2.27, 'clicks': 539.15, 'ctr': 0.08, 'impressions': 7048.56, 'totalCost': 45.63, 'rate': 52083.99700000001, 'source': 'semantics'}, {'text': 'sports', 'competition': 'High', 'volume': 381030, 'avgVolume': 306000, 'relevance': 0.339, 'suggestedBid': 0.37, 'avgCpc': 0.57, 'avgPosition': 1.56, 'clicks': 3066.13, 'ctr': 0.03, 'impressions': 100405.47, 'totalCost': 1758.91, 'rate': 42114.44900000001, 'source': 'original'}, {'text': 'van', 'competition': 'High', 'volume': 341360, 'avgVolume': 313522, 'relevance': 0.013, 'suggestedBid': 0.87, 'avgCpc': 0.72, 'avgPosition': 1.38, 'clicks': 4847.18, 'ctr': 0.05, 'impressions': 88685.28, 'totalCost': 3473.73, 'rate': 40653.1088, 'source': 'semantics'}, {'text': 'baseball', 'competition': 'High', 'volume': 82960, 'avgVolume': 77688, 'relevance': 0.0, 'suggestedBid': 0.26, 'avgCpc': 0.44, 'avgPosition': 1.88, 'clicks': 2937.13, 'ctr': 0.03, 'impressions': 89521.05, 'totalCost': 1300.94, 'rate': 23929.849400000003, 'source': 'semantics'}, {'text': 'chess', 'competition': 'High', 'volume': 128670, 'avgVolume': 219061, 'relevance': 0.013, 'suggestedBid': 0.17, 'avgCpc': 0.07, 'avgPosition': 1.98, 'clicks': 270.78, 'ctr': 0.03, 'impressions': 10555.39, 'totalCost': 19.27, 'rate': 17499.537800000002, 'source': 'semantics'}, {'text': 'battery', 'competition': 'High', 'volume': 85340, 'avgVolume': 99234, 'relevance': 0.116, 'suggestedBid': 0.89, 'avgCpc': 0.85, 'avgPosition': 1.92, 'clicks': 1904.84, 'ctr': 0.05, 'impressions': 40713.75, 'totalCost': 1620.45, 'rate': 15470.2032, 'source': 'semantics'}, {'text': 'stamp', 'competition': 'High', 'volume': 8150, 'avgVolume': 9620, 'relevance': 0.0, 'suggestedBid': 0.52, 'avgCpc': 0.86, 'avgPosition': 2.45, 'clicks': 2736.19, 'ctr': 0.05, 'impressions': 55663.57, 'totalCost': 2342.49, 'rate': 12353.4346, 'source': 'competitors'}, {'text': 'motor car', 'competition': 'High', 'volume': 400, 'avgVolume': 399, 'relevance': 0.05, 'suggestedBid': 0.09, 'avgCpc': 0.6, 'avgPosition': 1.08, 'clicks': 1888.36, 'ctr': 0.03, 'impressions': 57007.58, 'totalCost': 1135.94, 'rate': 11807.191, 'source': 'semantics'}, {'text': 'automobile', 'competition': 'High', 'volume': 8650, 'avgVolume': 6652, 'relevance': 0.0, 'suggestedBid': 3.88, 'avgCpc': 0.16, 'avgPosition': 1.18, 'clicks': 14257.24, 'ctr': 0.35, 'impressions': 40902.26, 'totalCost': 2336.89, 'rate': 11497.6406, 'source': 'semantics'}, {'text': 'team', 'competition': 'High', 'volume': 42210, 'avgVolume': 84872, 'relevance': 0.0, 'suggestedBid': 0.14, 'avgCpc': 0.41, 'avgPosition': 1.31, 'clicks': 104.76, 'ctr': 0.01, 'impressions': 11987.36, 'totalCost': 42.82, 'rate': 8359.511600000002, 'source': 'semantics'}, {'text': '4wd', 'competition': 'High', 'volume': 5470, 'avgVolume': 4338, 'relevance': 0.16, 'suggestedBid': 0.48, 'avgCpc': 0.58, 'avgPosition': 2.06, 'clicks': 2415.18, 'ctr': 0.08, 'impressions': 31085.85, 'totalCost': 1395.61, 'rate': 7003.9698, 'source': 'semantics'}, {'text': 'sedan', 'competition': 'High', 'volume': 5570, 'avgVolume': 8370, 'relevance': 0.018, 'suggestedBid': 1.47, 'avgCpc': 1.67, 'avgPosition': 1.13, 'clicks': 1114.67, 'ctr': 0.04, 'impressions': 26971.53, 'totalCost': 1858.63, 'rate': 6203.272800000001, 'source': 'semantics'}, {'text': 'england', 'competition': 'High', 'volume': 31010, 'avgVolume': 37285, 'relevance': 0.0, 'suggestedBid': 0.24, 'avgCpc': 0.2, 'avgPosition': 1.14, 'clicks': 24.2, 'ctr': 0.0, 'impressions': 12675.41, 'totalCost': 4.78, 'rate': 5149.905000000001, 'source': 'semantics'}, {'text': 'driver', 'competition': 'High', 'volume': 39920, 'avgVolume': 38572, 'relevance': 0.101, 'suggestedBid': 0.12, 'avgCpc': 0.71, 'avgPosition': 1.26, 'clicks': 295.42, 'ctr': 0.03, 'impressions': 10093.38, 'totalCost': 210.6, 'rate': 4777.889800000001, 'source': 'semantics'}, {'text': 'suspension', 'competition': 'High', 'volume': 6250, 'avgVolume': 8290, 'relevance': 0.058, 'suggestedBid': 0.73, 'avgCpc': 0.77, 'avgPosition': 2.23, 'clicks': 794.37, 'ctr': 0.05, 'impressions': 16995.61, 'totalCost': 615.3, 'rate': 4138.3848, 'source': 'semantics'}, {'text': 'boot', 'competition': 'High', 'volume': 14150, 'avgVolume': 17351, 'relevance': 0.113, 'suggestedBid': 0.34, 'avgCpc': 0.53, 'avgPosition': 1.6, 'clicks': 607.45, 'ctr': 0.05, 'impressions': 12841.83, 'totalCost': 323.95, 'rate': 3904.5114000000003, 'source': 'semantics'}]
        return render_template('keywords.html', result=keywords)
    return render_template('keywords.html')


@app.route("/competitors", methods=['POST', 'GET'])
def findCompetitors():
    if request.method == 'POST':
        result = request.form
        url = result['URL']
        # title, article, k_1 = scrap(url)
        # competitors = Competitor_Main.get_comps(url, title, article)
        competitors=[{'url': 'https://www.autoexpress.co.uk/best-cars/103133/best-new-cars-for-2020', 'reach': 60, 'similarity': 0.999}, {'url': 'https://www.garo.ie/cms/cms.jsp?menu_id=34963', 'reach': -1, 'similarity': 0.115}, {'url': 'https://www.autoexpress.co.uk/best-cars/103133/best-new-cars-for-2020/page/0/4', 'reach': 60, 'similarity': 0.284}, {'url': 'https://teslamotorsclub.com/tmc/threads/vw-will-trample-tesla.109291/page-7', 'reach': 40, 'similarity': 0.066}, {'url': 'https://www.autoexpress.co.uk/best-cars/103133/best-new-cars-for-2020/page/0/3', 'reach': 60, 'similarity': 0.284}, {'url': 'https://teslamotorsclub.com/tmc/threads/vw-will-trample-tesla.109291/page-8', 'reach': 40, 'similarity': 0.084}, {'url': 'https://www.lse.co.uk/ShareChat.asp?ShareTicker=AML&share=Aston-Martin-Lagonda&thread=1D12CC4C-1A61-43B8-BDE9-5C330883735E', 'reach': 3, 'similarity': 0.100}, {'url': 'http://static.autoexpress.co.uk/authors/jonathan-burn', 'reach': 60, 'similarity': 0.035}, {'url': 'https://www.geekzone.co.nz/forums.asp?forumid=162&topicid=197896&page_no=93', 'reach': 5, 'similarity': 0.096}, {'url': 'https://www.carusa.info/new-honda-cars-for-2020/', 'reach': 2, 'similarity': 0.051}, {'url': 'https://www.carbuyer.co.uk/news/167673/best-new-cars-coming-in-2020', 'reach': 30, 'similarity': 0.257}, {'url': 'https://www.driving.co.uk/news/features/best-new-cars-coming-2020/', 'reach': -1, 'similarity': 0.213}, {'url': 'https://www.autocar.co.uk/slideshow/global-preview-best-new-cars-coming-2020-and-beyond-0', 'reach': 60, 'similarity': 0.089}, {'url': 'https://cars.usnews.com/cars-trucks/future-cars', 'reach': 430, 'similarity': 0.012}, {'url': 'https://www.carwow.co.uk/news/4498/geneva-motor-show-best-new-cars-coming-2020', 'reach': 10, 'similarity': 0.212}, {'url': 'https://www.autoguide.com/auto-news/2020/01/top-10-most-anticipated-new-cars-coming-in-2020.html', 'reach': 20, 'similarity': 0.231}, {'url': 'https://www.esquire.com/uk/design/g30563856/best-cars-2020/', 'reach': 210, 'similarity': 0.230}, {'url': 'https://www.consumerreports.org/new-cars/new-cars-on-the-horizon/', 'reach': 170, 'similarity': 0.019}, {'url': 'https://www.kbb.com/best-cars/top-10-our-10-favorite-new-2020-cars/', 'reach': 310, 'similarity': 0.078}]

        return render_template('competitors.html', result=competitors)
    return render_template('competitors.html')


if __name__ == '__main__':
    app.run(debug=True)

