import os
import random
import time
from contextlib import closing

import requests


def chunk_download(Url, name=None, markpath=None, headers=[]):
    # 目录
    path = os.getcwd() + os.sep + "images" + os.sep
    if markpath is not None:
        path = path + markpath + os.sep

    # 文件后缀
    ext = Url[-4:]
    exts = ['.jpg', '.png', '.gif']
    if ext not in exts:
        ext = '.jpg'
    try:
        # 递归创建目录
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        # 保存文件名称
        if name is None:
            name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(10000, 99999)) + ext
        # 目录文件名
        pathName = path+name
        if not os.path.exists(pathName):
            with closing(requests.get(Url, headers=headers, stream=True)) as response:
                with open(pathName, 'wb') as fd:
                    for chunk in response.iter_content(128):
                        fd.write(chunk)
            return pathName
        else:
            return pathName

    except Exception as e:
        return e



if __name__  == '__main__':
    url = "http://image.nationalgeographic.com.cn/2017/1122/20171122113404332.jpg"
    pathname=chunk_download(url)
    print(pathname)