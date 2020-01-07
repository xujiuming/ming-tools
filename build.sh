#!/bin/bash

sudo rm -rf ./build
sudo rm -rf ./dist

# 打包
python setup.py sdist
python setup.py bdist_wheel
#上传到 pipy python3 twt
twine upload dist/*

