#!/bin/bash

sudo rm -rf ./build
sudo rm -rf ./dist
sudo rm -rf ./jiuming_tools.egg-info

# 打包
python setup.py sdist
python setup.py bdist_wheel
#上传到 pipy python3 twt
pip3 install twine
twine upload dist/*

