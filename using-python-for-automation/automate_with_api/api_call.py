import requests
import json

base_url = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '012993441012'}
response = requests.get(base_url, params=parameters)
print(response.url)

content = response.content
info = json.loads(content)
item = info["items"]
item_info = item[0]
title = item_info["title"]
brand = item_info["brand"]
print(title)
print(brand)
