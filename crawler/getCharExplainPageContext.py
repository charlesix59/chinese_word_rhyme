from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
url = "https://zh.wiktionary.org/zh-hant/User:Wihwang/%E5%8F%A4%E6%BC%A2%E8%AA%9E%E5%B8%B8%E7%94%A8%E5%AD%97%E5%AD%97" \
      "%E5%85%B8 "

proxy = '127.0.0.1:7890'
proxies = {
    "http": "http://%(proxy)s/" % {'proxy': proxy},
    "https": "http://%(proxy)s/" % {'proxy': proxy}
}

f = requests.get(url, headers=headers, proxies=proxies)

soup = BeautifulSoup(f.text, 'html.parser')

text = soup.find("pre")

with open("charExplain.txt", "w", encoding="utf-8") as f:
    f.write(text.string)
