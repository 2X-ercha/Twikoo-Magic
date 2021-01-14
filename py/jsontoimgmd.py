import json

with open("./twikoo/hahaha.json", "r", encoding='utf-8') as j:
    data = json.load(j)
# print(data)
data = data['阿狸']['container']
print(data)
for src in data:
    print("![]("+src['icon'][10:-2]+")")