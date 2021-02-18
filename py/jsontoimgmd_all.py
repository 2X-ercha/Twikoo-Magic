import json
import os

classlist = os.listdir("./image/")

for classname in classlist:
    # "./Classification/"+classname+"/"
    try: os.mkdir("./Classification/"+classname+"/")
    except: pass

    filenamelist = os.listdir("./image/"+classname)
    url = "https://cdn.jsdelivr.net/gh/2x-ercha/twikoo-magic/image/" + classname + "/"

    with open("./Classification/"+classname+"/README.md", "w", encoding="utf-8") as f:
        f.write(classname+"\n\n")
        for filename in filenamelist:
            f.write("![](" + url + filename + ")\n")
    