import requests

keyword = input("商品名を入力してください:")
# searchJanCode = '4902370542912'
#URL設定
YahooItemSearchURL = "https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch"


#辞書設定
params = {}
params ['appid'] = 'dj00aiZpPTdpT2VIRUxmWGpsdiZzPWNvbnN1bWVyc2VjcmV0Jng9ZmI-'
# params ['jan_code'] = searchJanCode
params ['query'] = keyword

response = requests.get(YahooItemSearchURL,params)
results = response.json()

Yitems = results['totalResultsAvailable']
YitemName = results['hits'][0]['name']
Yprice = results['hits'][0]['price']
Ytax = results['hits'][0]['priceLabel']['taxable']
Yreview = results['hits'][0]['review']['rate']
Ybrand = results['hits'][0]['brand']['name']

print(Yitems,YitemName,Yprice,Ytax,Yreview,Ybrand)