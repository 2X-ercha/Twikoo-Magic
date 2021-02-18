import json

with open("owo_beau.json", "r", encoding="utf-8") as owo_beau:
    owo_beau = json.load(owo_beau)
with open("owo.json", "w", encoding="utf-8") as owo:
    owo.write(json.dumps(owo_beau, ensure_ascii=False))