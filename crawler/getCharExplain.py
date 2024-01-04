import re

import json

res = {}

littleNumArr = ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩", "⑾", "⑿", "⒀", "⒁", "⒂", "⒃", "⒄", "⒅", "⒆", "⒇"]

char = ""
pron = ""
pronounceArr = []
explainArr = []

with open("charExplain.txt", "r", encoding="utf-8") as f:
    text = f.read()

for paragraph in text.split("\n"):
    if paragraph == "":
        pronounceArr.append({"pronunciation": pron, "explains": explainArr})
        res[char] = pronounceArr
        char = ""
        pron = ""
        pronounceArr = []
        explainArr = []
    if char == "":
        char = paragraph
        continue
    if paragraph[0] not in littleNumArr:
        # 如果之前已经有过发音，则将之前的发音暂存
        if pron != "":
            pronounceArr.append({"pronunciation": pron, "explains": explainArr})
            pron = ""
            explainArr = []
        pron = paragraph
        pattern = re.compile('[\u4e00-\u9fff<【]+')
        result = pattern.search(pron)
        if result:
            index = result.span(0)[0]
            print(str(index) + " " + pron)
            explainArr.append(pron[index:])
            pron = pron[:index]
    else:
        explainArr.append(paragraph[1:])

with open("explain.json", "w", encoding="utf-8") as json_file:
    json.dump(res, json_file, ensure_ascii=False, indent=4)

