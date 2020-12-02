#!/bin/python3
# author ming
import os

if __name__ == '__main__':
    # 读取 $PATH
    bin_path_str_arr = os.getenv("PATH").split(":")
    cmd_name_set = set()
    for bin_path in bin_path_str_arr:
        for f in os.listdir(bin_path):
            cmd_name_set.add(f)
    print(cmd_name_set)
    print(len(cmd_name_set))
    print("cat" in cmd_name_set)
