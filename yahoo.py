import requests

keyword = input("商品名を入力してください:")

# 検索対象のJANコード
# searchJanCode = '0194397490312'
YahooItemSearchURL = "https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch"

params = {}
params ['appid'] = 'dj00aiZpPTdpT2VIRUxmWGpsdiZzPWNvbnN1bWVyc2VjcmV0Jng9ZmI-'

# params ['jan_code'] = searchJanCode
params ['query'] = keyword
# params ['hits'] = 20

response = requests.get(YahooItemSearchURL,params)
results = response.json()


for i in results(20):
    # ヒット数
    Yitems = results['totalResultsAvailable']
    # 商品名
    YitemName = results['hits'][i]['name']
    # 商品価格
    Yprice = results['hits'][i]['price']

    print(Yitems)
    print(YitemName)
    print(Yprice)