#!/bin/bash


mkdir ~/.pip
cat > ~/.pip/pip.conf << EOF
[global]
trusted-host=mirrors.aliyun.com
index-url=https://mirrors.aliyun.com/pypi/simple/
EOF
pip3 install pipenv
pip3 install setuptools
export PATH=$PATH:~/.local/bin
pipenv shell