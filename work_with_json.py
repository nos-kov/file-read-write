import json

with open("news.json", encoding = "utf-8") as f:
    json_data = json.load(f)
    print (json_data)
    print(type(json_data))