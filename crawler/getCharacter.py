from bs4 import BeautifulSoup
import requests
import json

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
url = "https://zh.wikisource.org/zh-hans/%E5%B9%B3%E6%B0%B4%E9%9F%BB"

proxy = '127.0.0.1:7890'
proxies = {
    "http": "http://%(proxy)s/" % {'proxy': proxy},
    "https": "http://%(proxy)s/" % {'proxy': proxy}
}

res = {}

f = requests.get(url, headers=headers, proxies=proxies)

soup = BeautifulSoup(f.text, 'html.parser')
for span in soup.find_all("span", class_="mw-headline"):
    cage = span.get("id")
    h2 = span.parent
    nav_type = type(h2.next_sibling)
    p = h2.next_sibling.next_sibling
    chunk = {}
    while p and type(p) != nav_type and p.get("class") != "mw-headline":
        part = p.string.rstrip()
        print(part)
        p = p.next_sibling
        text = p.string.rstrip()
        p = p.next_sibling
        if p.string[0] != "【":
            continue
        text += p.string[3:].rstrip()
        p = p.next_sibling
        if p.string[0] == "【":
            text += p.string[3:].rstrip()
            p = p.next_sibling
        chunk[part] = list(text)
    res[cage] = chunk

with open("pingshui.json", "w", encoding="utf-8") as json_file:
    json.dump(res, json_file, ensure_ascii=False, indent=4)

print(res)
