import os
import requests

headers = {
    "Cookie": "arccount62298=c; arccount62019=c",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
}
while 1:
    dicname = input()

    try: 
        os.mkdir("./py/newimage/"+dicname)
    except: 
        pass

    os.chdir("./py/newimage/"+dicname)

    while 1:
        s=input()
        if s=="0":break
        s = s.split("(")
        url = s[-1][:-1]
        name = url.split("/")
        name = name[-1]
        with open(name, "wb") as img:
            img.write(requests.get(url, headers=headers).content)
            print("已保存"+name)
    
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")