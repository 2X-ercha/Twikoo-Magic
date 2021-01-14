import json

with open("./twikoo/weisuomeng.json", "r", encoding='utf-8') as j:
    data = json.load(j)
# print(data)
data = data['猥琐萌']['container']
print(data)
for src in data:
    print("![]("+src['icon'][10:-2]+")")