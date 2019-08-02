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
    'Referer': "http://www.mzitu.com/99566",
    'Cookie': "Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1564754055,1564754120,1564754207; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1564755195",

}



# 获取页面html
def GetHtml(url):
    try:
        requests.packages.urllib3.disable_warnings()
        return requests.get(url, headers=headers, verify=False).text
    except:
        print(url+"异常")
        return None



# 定义一个解析妹子总页面的方法，来获取单个妹子的链接
def parseHtml(html):
    soup = BeautifulSoup(html, "lxml")
    return soup.select("a[target='_blank']")


# 获取妹子的图片
def get_pic(imageUrl):
    print(imageUrl + "正在解析...")
    imageHtml = GetHtml(imageUrl)
    if imageHtml is not None:
        soup = BeautifulSoup(imageHtml, "lxml")
        imgsrc = soup.find("div", class_="main-image").find_all("img")
        # 标题进行md5加密
        str = imgsrc[0]["src"]
        m = hashlib.md5()
        m.update(str.encode())
        m.hexdigest()
        imgtitle = m.hexdigest()

        # 图片标题 将？转——
        signpath = soup.find("h2", class_="main-title").get_text().replace('?','_')
        if "（" in signpath:
            signpath = signpath[:signpath.index("（")]

        if imgtitle is None:
            downloadImg(imgsrc[0]["src"])
        downloadImg(imgsrc[0]["src"], imgtitle, signpath)
        # time.sleep(2)


# https://www.mzitu.com/179288
# 获取页面有多少下一页
def get_pic_num(listUrl ):
    html=GetHtml(listUrl)
    if html is not  None:
        soup = BeautifulSoup(html, "lxml")
        list = soup.find("div", class_="pagenavi").find_all("span")
        return int(list[-2].string)
    return 0


# 下载图片(单线程)
def downloadImg(imgeurl, name=None, signpath=''):
    print(imgeurl + "正在下载图片...")

    requests.packages.urllib3.disable_warnings()

    img = requests.get(imgeurl, headers=headers, verify=False)
    # img = GetHtml(imgeurl)
    if img is not None:
        paths = os.getcwd() + os.sep + "image" + os.sep + signpath + os.sep
        # 判断路径是否存在
        if not os.path.exists(paths):
            os.makedirs(paths)
        if name is None:
            name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(10000, 99999)) + ".jpg"
        else:
            # name = name + str(random.randint(100, 999)) + ".jpg"
            name = name + ".jpg"

        if not os.path.isfile(paths + name):
            with open(paths + name, 'ab') as f:
                f.write(img.content)
                print(paths + name + "下载完成")

def run():
    url = "http://www.mzitu.com/all"
    # pic = "http://www.mzitu.com/108528"
    htmls = GetHtml(url)
    pics=[]
    for html in parseHtml(htmls):
        pics.append(html["href"])
    pic = random.sample(pics,1)[0]
    for i in range(get_pic_num(pic)):
        listUrl = "{}{}{}".format(pic, "/", i+1)
        t = threading.Thread(target=get_pic, args=(listUrl,))
        t.start()
        t.join()

if __name__ == "__main__":
    run()