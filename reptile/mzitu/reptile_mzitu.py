
import hashlib
import os
import random
import threading
import time
import requests
from bs4 import BeautifulSoup

from multiprocessing import Pool, Process

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

# 获取妹子的图片并下载
def put_childurl(childurl):
    print(childurl + "正在解析...")
    imageHtml = GetHtml(childurl)
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



# 下载图片(单线程)
def downloadImg(imgeurl, name=None, signpath=''):
    print(imgeurl + "正在下载图片...")
    requests.packages.urllib3.disable_warnings()
    img = requests.get(imgeurl, headers=headers, verify=False)
    # img = GetHtml(imgeurl)
    if img is not None:
        paths = os.getcwd() + os.sep + "images" + os.sep + signpath + os.sep
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


# 获取总共的url
def get_fatherurl():
    url = "http://www.mzitu.com/all"
    father_Url = []
    htmls = GetHtml(url)
    if htmls is not None:
        soup = BeautifulSoup(htmls, "lxml")
        parseHtml = soup.select("a[target='_blank']")
        for html in parseHtml:
            father_Url.append(html["href"])
    return father_Url

# 根据url获取总共有多少图片可以下载
def fatherurl_Get_childurl(fatherUrl):
    # "http://www.mzitu.com/108528"
    child_url =[]
    html = GetHtml(fatherUrl)
    if html is not  None:
        soup = BeautifulSoup(html, "lxml")
        list = soup.find("div", class_="pagenavi").find_all("span")
        child_num =int(list[-2].string)
        for i in range(child_num):
            listUrl = "{}{}{}".format(fatherUrl, "/", i + 1)
            child_url.append(listUrl)
    return child_url




if __name__ == "__main__":
    fatherurl = get_fatherurl()
    # 去除最后一个
    fatherurl.pop()
    fatherurl.reverse()
    for furl in fatherurl:
        childurl =fatherurl_Get_childurl(furl)


        childurllen = len(childurl)
        for i in range(childurllen):

            # 产生线程的实例
            t = threading.Thread(target=put_childurl, args=(childurl[i],))
            # 线程守护
            t.setDaemon(True)
            t.start()
            t.join()

        # for i in range(childurllen):
            # 进程
            # p = Process(target=put_childurl, args=(childurl[i],))
            # p.start()
            # p.join()


