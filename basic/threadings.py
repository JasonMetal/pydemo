import threading
import time

urls =[
    "https://www.baidu.com",
    "https://www.oschina.net"
]


def sleepweb(index, url):
    print("start url"+url+" at:"+str(time.time()))
    time.sleep(5)
    print("End url:"+url+" at:"+str(time.time()))

if __name__ == "__main__":
    # urlslen = range(len(urls))
    # for i in urlslen:
    #     sleepweb(i,urls[i])
    # print("ALL done at"+str(time.time()))

    # 线程列表，用例存放线程
    threads = []
    urlslen=range(len(urls))
    for i in urlslen:
        # 产生线程的实例
        t = threading.Thread(target=sleepweb, args=(i, urls[i], ))
        # 线程守护
        t.setDaemon(True)
        threads.append(t)
    for i in urlslen:
        # 循环列表，依次执行各个子线程
        threads[i].start()
    for i in urlslen:
        # 将最后一个子线程阻塞主线程，只有当该子线程完成后主线程才能往下执行
        threads[i].join()
    print("ALL done at"+str(time.time()))