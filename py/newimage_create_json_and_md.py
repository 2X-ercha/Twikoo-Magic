import json
import os

classlist = os.listdir("./py/newimage/")

for classname in classlist:
    # 创建新图片的github源owo.json
    try: os.mkdir("./Classification/"+classname+"/")
    except: pass

    filenamelist = os.listdir("./py/newimage/"+classname)
    url = "https://cdn.jsdelivr.net/gh/2x-ercha/twikoo-magic@master/image/" + classname + "/"

    classjson = {}
    classjson["type"]="image"
    container = []
    num = 1
    for filename in filenamelist:
        img = {}
        img["text"]=classname + "-" +str(num)
        num+=1
        img["icon"]="<img src='" + url + filename + "'>"
        container.append(img)
    classjson["container"]=container
    owojson={}
    owojson[classname]=classjson

    with open("./Classification/"+classname+"/"+classname+".json", "w", encoding="utf-8") as owo:
        owo.write(json.dumps(owojson, indent=2, separators=(',', ':'), ensure_ascii=False))

for classname in classlist:
    # 创建新图片的oss源owo.json
    try: os.mkdir("./Class_oss/"+classname+"/")
    except: pass

    filenamelist = os.listdir("./py/newimage/"+classname)
    url = "https://twikoo-magic.oss-cn-hangzhou.aliyuncs.com/" + classname + "/"

    classjson = {}
    classjson["type"]="image"
    container = []
    num = 1
    for filename in filenamelist:
        img = {}
        img["text"]=classname + "-" +str(num)
        num+=1
        img["icon"]="<img src='" + url + filename + "'>"
        container.append(img)
    classjson["container"]=container
    owojson={}
    owojson[classname]=classjson

    with open("./Class_oss/"+classname+"/"+classname+".json", "w", encoding="utf-8") as owo:
        owo.write(json.dumps(owojson, indent=2, separators=(',', ':'), ensure_ascii=False))

for classname in classlist:
    # 创建新图片的github源README.md
    filenamelist = os.listdir("./py/newimage/"+classname)
    url = "https://cdn.jsdelivr.net/gh/2x-ercha/twikoo-magic@master/image/" + classname + "/"

    # Classification文件夹
    with open("./Classification/"+classname+"/"+"README.md", "w", encoding="utf-8") as md:
        md.write("# " + classname + "表情包\n\n")
        for filename in filenamelist:
            md.write("![](" + url + filename +")\n")
    
    # Class_oss文件夹
    with open("./Class_oss/"+classname+"/"+"README.md", "w", encoding="utf-8") as md:
        md.write("# " + classname + "表情包\n\n")
        for filename in filenamelist:
            md.write("![](" + url + filename +")\n")