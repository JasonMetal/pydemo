### pip简介

pip是Python包管理工具，该工具提供了对Python包的查找、下载、安装、卸载的功能。
web搜索包 https://pypi.org

### 檢查是否安裝并查看版本
~~~
pip --version
~~~

### 常见的命令
~~~
获取帮助
pip --help

升级 pip
pip install -U pip

安装包
pip install requests              # 最新版本
pip install requests==19.2       # 指定版本
pip install 'requests>=1.0'     # 最小版本

升级包
pip install --upgrade requests

卸载包
pip uninstall requests

搜索包
pip search requests

显示安装包信息
pip show 

查看指定包的详细信息
pip show -f requests

列出已安装的包
pip list

查看可升级的包
pip list -o
~~~

### 项目包管理
#### 生成requirements.txt文件
~~~
pip freeze > requirements.txt
~~~
#### 安装requirements.txt依赖
~~~
pip install -r requirements.txt
~~~
