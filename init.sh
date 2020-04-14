#!/bin/bash

mkdir ~/.pip
cat >~/.pip/pip.conf <<EOF
[global]
trusted-host=mirrors.aliyun.com
index-url=https://mirrors.aliyun.com/pypi/simple/
EOF
pip3 install pipenv
pip3 install setuptools
export PATH=$PATH:~/.local/bin
pipenv shell

# 打包
python setup.py sdist
python setup.py bdist_wheel
#上传到 pipy python3 twt
pip3 install twine
twine upload dist/*

# 临时安装本地目录
pip3 install --editable .
