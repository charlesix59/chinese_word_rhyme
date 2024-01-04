import re
import time

from bs4 import BeautifulSoup
import requests
import json

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
maxId = 818
proxy = '127.0.0.1:7890'
baseUrl = "https://sou-yun.cn/QueryCiTune.aspx?id="
pattern = r"<span class=\"rhythm\">.</span>"
replacePatten = r"<span class=\"comment\">(.*?)</span>"
replacement = r"\1"
res = {}

for i in range(0, maxId):
    url = baseUrl + str(i)
    f = requests.get(url, headers=headers)
    soup = BeautifulSoup(f.text, 'html.parser')
    # 获取词牌名
    name = soup.find("span", class_="ciTuneName").string
    formats = soup.find_all("div", class_="ciTuneFormat")
    descs = soup.find_all("div", class_="ciTuneDesc")
    topDesc = descs.pop(0).find("span", class_="comment").string
    ciFormats = []
    for tFormat, desc in zip(formats, descs):
        tuneFormat = {}
        formatDesc = tFormat.find("span", class_="tuneFormatDesc").string
        formatAuthor = tFormat.find("span", class_="indentLabel").string
        tunesArr = tFormat.find_all("span", class_="comment")
        ciTunes = []
        for tunes in tunesArr:
            rhythms = tunes.find_all("span", class_="rhythm")
            tunes = str(tunes)
            tunes = re.sub(pattern, " ", tunes)
            tunes = re.sub(replacePatten, replacement, tunes).strip()
            for char in tunes:
                if char == " ":
                    ciTunes[-1]["rhythm"] = rhythms.pop(0).string
                    continue
                ciTunes.append({"tune": char})
            # 结束之后赋值最后一个字的韵并赋换行
            ciTunes[-1]["rhythm"] = rhythms.pop(0).string
            ciTunes[-1]["shift"] = "true"
        ciFormats.append({
            "sketch": formatDesc,
            "author": formatAuthor,
            "tunes": ciTunes,
            "desc": desc.string
        })
    res[name] = {
        "desc": topDesc,
        "formats": ciFormats
    }
    time.sleep(1)
    print("解析 %d %s 结束" % (i, name))
    time.sleep(3)

with open("Ci_Tunes.json", "w", encoding="utf-8") as json_file:
    json.dump(res, json_file, ensure_ascii=False, indent=4)
