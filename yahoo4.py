import requests
import json

keyword = input('キーワード-->')

url = 'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch'

params = {}
params ['appid'] = 'dj00aiZpPTdpT2VIRUxmWGpsdiZzPWNvbnN1bWVyc2VjcmV0Jng9ZmI-'
params ['query'] = keyword
params ['results'] = 20

call = requests.get(url,params)
results = call.json()

# res_dict = json.loads(call.content)
# count = len(res_dict['hits'])

for i in results:
   print("商品名：", ['hits'][i]['name'])
   print("価格：", ['hits'][i]['price'])
   print("商品URL", ['hits'][i]['url'])
   print()