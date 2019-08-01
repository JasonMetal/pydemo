import _thread
import hashlib
import os
import random
import threading
import time
import requests
from bs4 import BeautifulSoup



headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
    'Connection': 'Keep-Alive',
    'Referer': "http://www.mzitu.com/99566"
}


# 获取页面html
def GetHtml(url):
    requests.packages.urllib3.disable_warnings()
    return requests.get(url, headers=headers,verify=False).text


# 定义一个解析妹子总页面的方法，来获取单个妹子的链接
def parseHtml(html):
    soup = BeautifulSoup(html, "lxml")
    return soup.select("a[target='_blank']")


# 获取妹子的图片
def get_pic(listimageUrl):
    print(listimageUrl + "正在解析...")
    listhtml = GetHtml(listimageUrl)

    soup = BeautifulSoup(listhtml, "lxml")
    imgsrc = soup.find("div", class_="main-image").find_all("img")


    # 标题进行md5加密
    str = imgsrc[0]["src"]
    m = hashlib.md5()
    m.update(str.encode())
    m.hexdigest()
    imgtitle = m.hexdigest()

    # 图片标题 将？转——
    # imgtitle = str(soup.find("h2", class_="main-title").get_text()).replace("?",'_')
    if imgtitle is None:
        downloadImg(imgsrc[0]["src"])
    downloadImg(imgsrc[0]["src"], imgtitle)
    # time.sleep(1)

# https://www.mzitu.com/179288
# 获取页面有多少下一页
def get_pic_num(listUrl):
    html=GetHtml(listUrl)
    soup = BeautifulSoup(html, "lxml")
    list = soup.find("div", class_="pagenavi").find_all("span")
    return int(list[-2].string)


# 下载图片(单线程)
def downloadImg(imgeurl, name=None, signpath=''):
    print(imgeurl + "正在下载图片...")
    img = requests.get(imgeurl, headers=headers)
    # img = GetHtml(imgeurl)
    paths = os.getcwd() + os.sep + "image" + os.sep + signpath
    # 判断路径是否存在
    if not os.path.exists(paths):
        os.makedirs(paths)
    if name is None:
        name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(10000, 99999)) + ".jpg"
    else:
        name = name + str(random.randint(100, 999)) + ".jpg"

    if not os.path.isfile(paths + name):
        with open(paths + name, 'ab') as f:
            f.write(img.content)
            print(paths + name + "下载完成")





print("下载开始")
url = "http://www.mzitu.com/all"
pic = "http://www.mzitu.com/108528"
htmls = GetHtml(url)
for html in parseHtml(htmls):
    print(html["href"],html.get_text())
    for i in range(get_pic_num(html["href"])):
        listUrl = "{}{}{}".format(pic, "/", i + 1)
        get_pic(listUrl)
        # t = threading.Thread(target=get_pic, args=(listUrl,))
        # t.start()
        # t.join()
print("下载结束")


