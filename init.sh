#!/bin/bash

mkdir ~/.pip
cat >~/.pip/pip.conf <<EOF
[global]
trusted-host=mirrors.aliyun.com
index-url=https://mirrors.aliyun.com/pypi/simple/
EOF
# 关闭 pip.conf配置
mv ~/.pip/pip.conf ~/.pip/pip.conf.bak
#重新打开pip.conf
mv ~/.pip/pip.conf.bak ~/.pip/pip.conf

# 安装 pipenv  twine  setuptools
pip3 install pipenv twine setuptools wheel
export PATH=$PATH:~/.local/bin
# 打包
python setup.py sdist bdist_wheel
#上传到 pipy python3 twt
twine upload dist/*

# 临时安装本地目录
# 临时安装本地目录
pip3 install --editable .
