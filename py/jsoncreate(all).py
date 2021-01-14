import json
import os

classlist = os.listdir("./image/")

for classname in classlist:
    # "./Classification/"+classname+"/"
    try: os.mkdir("./Classification/"+classname+"/")
    except: pass

    filenamelist = os.listdir("./image/"+classname)
    url = "https://cdn.jsdelivr.net/gh/2x-ercha/twikoo-magic/image/" + classname + "/"

    classjson = {}
    classjson["type"]="image"
    container = []
    num = 1
    for filename in filenamelist:
        img = {}
        img["text"]=classname + "-" +str(num)
        num+=1
        img["icon"]="<img src=" + url + filename + ">"
        container.append(img)
    classjson["container"]=container
    owojson={}
    owojson[classname]=classjson

    with open("./Classification/"+classname+"/"+classname+".json", "w", encoding="utf-8") as owo:
        owo.write(json.dumps(owojson, indent=2, separators=(',', ':'), ensure_ascii=False))
