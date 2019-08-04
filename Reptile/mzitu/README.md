### 简介
pip 是 Python 包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。

### 安装
无论是Windwos还是Centos安装，默认情况下都是安装pip工具

##### 获取帮助
~~~
pip --help
~~~
##### 升级 pip
~~~
pip install -U pip
~~~
##### 安装包
~~~
pip install requests              # 最新版本
pip install requests==1.0.0       # 指定版本
pip install requests>=1.0.0'     # 最小版本
~~~
##### 升级包
~~~
pip install --upgrade requests
~~~
##### 卸载包
~~~
pip uninstall requests
~~~
##### 搜索包
~~~
pip search  requests
~~~
##### 显示安装包信息
~~~
pip show 
~~~
##### 查看指定包的详细信息
~~~
pip show -f requests
~~~
##### 列出已安装的包
~~~
pip list
~~~
##### 查看可升级的包
~~~
pip list -o
~~~

##### 包迁移打包到requirements.txt
~~~
pip freeze >requirements.txt
~~~
##### 自动安装requirements.txt
~~~
pip install -r requirements.txt
~~~




