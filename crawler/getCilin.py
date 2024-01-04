import re

import json

res = {}

h1Patten = re.compile(r'第.*部')
h2Patten = re.compile(r'^.声')
linePatten = re.compile(r'【.*】')
linePatten2 = re.compile(r'（.*?）')

with open('CilinRaw.txt', 'r', encoding='utf-8') as file:
    # 将文件的所有行读取到列表中
    lines = file.readlines()
    part = ""
    tune = ""
    # 处理每一行
    for line in lines:
        if h1Patten.match(line):
            part = line
            res[part] = {}
            continue
        if h2Patten.match(line):
            tune = line[:2]
            res[part][tune] = []
            continue
        line = linePatten.sub("", line)
        line = linePatten2.sub("", line)
        arr = list(line)
        arr.pop()
        res[part][tune] += arr

with open("cilin.json", "w", encoding="utf-8") as json_file:
    json.dump(res, json_file, ensure_ascii=False, indent=4)

print(res)
