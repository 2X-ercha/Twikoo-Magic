import json

with open("twikoo/weisuomeng.json", "r", encoding="utf-8") as f:
    j = json.load(f)
with open("twikoo/weisuomeng.json", "w") as f:
    f.write(json.dumps(j, indent=2, separators=(',', ':')))