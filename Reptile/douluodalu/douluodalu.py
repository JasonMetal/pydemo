

import requests
from bs4 import BeautifulSoup


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Host" : "www.quanshuwang.com",
}


def getHtml(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = "gbk"
    return  resp.text

def parseHtml(url):
    html = getHtml(url)
    bf = BeautifulSoup(html, "lxml")
    return bf.find("div", class_="clearfix dirconone").find_all("a")


if __name__ =="__main__":
    urls = parseHtml("http://www.quanshuwang.com/book/44/44683")
    for item in urls:
        print(item.get("href")+item.get("title"))

