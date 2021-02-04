import json
import os

classlist = os.listdir("./image/")

for classname in classlist:
    # "./Classification/"+classname+"/"
    try: os.mkdir("./Class_hpp/"+classname+"/")
    except: pass

    filenamelist = os.listdir("./image/"+classname)
    url = "https://cdn.jsdelivr.net/gh/2x-ercha/twikoo-magic/" + classname + "/"

    classjson = {}
    classjson["type"]="image"
    container = []
    num = 1
    for filename in filenamelist:
        img = {}
        img["text"]=classname + "-" +str(num)
        num+=1
        img["icon"]="<img src=" + '"https://cdn.jsdelivr.net/gh/2x-ercha/twikoo-magic/loading.gif" data-src="' + url + filename + '">'
        container.append(img)
    classjson["container"]=container
    owojson={}
    owojson[classname]=classjson

    with open("./Class_hpp/"+classname+"/"+classname+".json", "w", encoding="utf-8") as owo:
        owo.write(json.dumps(owojson, indent=2, separators=(',', ':'), ensure_ascii=False))
