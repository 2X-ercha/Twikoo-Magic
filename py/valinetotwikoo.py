import json

with open("./py/valine/bilibiliHotKey.json", "r", encoding = 'utf-8') as valine:
    valine = json.load(valine)

twikoodic = {}
names = {}

emojiCDN = 'https://cdn.jsdelivr.net/gh/GamerNoTitle/ValineCDN@master/'

for value in valine.values():
    end = value.find("/")
    if value[:end] not in names.keys():
        names[value[:end]] = end

for name in names.keys():
    container = []
    for key,value in valine.items():
        if name == value[:names[name]]:
            dic = {}
            dic["icon"] = "<img src=" + emojiCDN + value + '>'
            dic["text"] = key
            container.append(dic)
    twikoodic[name]={"type": "emoticon","container": container}

with open("./py/twikoo/bilibiliHotKey.json", "w") as twikoo:
    twikoo.write(json.dumps(twikoodic, indent=2, separators=(',', ':')))
    
