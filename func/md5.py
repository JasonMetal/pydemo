import hashlib
def Pymd5(strings=''):
    # 如果是int类型转换成string类型
    if isinstance(strings,int):
        strings =str(strings)
    # 如果是float转string类型
    # if isinstance(strings,float):
    #     print("%f" %strings);
    resurt =hashlib.md5(strings.encode()).hexdigest()
    print(resurt)
    return resurt
