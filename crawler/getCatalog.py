from bs4 import BeautifulSoup
import requests
import json

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
url = "https://sou-yun.cn/QueryCiTune.aspx"
res = {}

f = requests.get(url, headers=headers)

soup = BeautifulSoup(f.text, 'html.parser')
for div in soup.find_all("div", class_="introduction"):
    ciType = div.find("span", class_="ciTuneName").string
    print(ciType)
    arr = []
    for inline in div.find_all("div", class_="inline1"):
        name = inline.find("a").string
        tunes = inline.find("span").string
        arr.append({"name": name, "tunes": tunes})
    res[ciType] = arr

with open("Pingshui_Catalog.json", "w", encoding="utf-8") as json_file:
    json.dump(res, json_file, ensure_ascii=False, indent=4)

print(res)
