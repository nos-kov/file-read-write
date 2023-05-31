import requests
from pprint import pprint

url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
result = {}

for element in resp.json():
    if element["name"] == "Hulk" or element["name"] == "Captain America" or element["name"] == "Thanos":
        result[element["name"]] = element["powerstats"]["intelligence"]
        
print(f' The most intelligent is: {sorted(result.items(), key=lambda x: x[1], reverse=True)[0][0]}')