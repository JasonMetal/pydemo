### Centos安装python3
~~~
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz
tar -xvJf Python-3.7.4.tar.xz
cd Python-3.7.4
./configure --prefix=/usr/local/python3 --enable-shared --enable-universalsdk --enable-optimizations
make && make install
echo "/usr/local/python3/lib" >> /etc/ld.so.conf.d/python3.conf && ldconfig
ln -s /usr/local/python3/bin/python3.7  /usr/bin/python3
ln -s /usr/local/python3/bin/pip3  /usr/bin/pip3
~~~

### window安装
~~~
https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe
~~~