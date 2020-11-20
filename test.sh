#!/bin/bash
# author ming
# 测试脚本 测试工具是否完善
mingmeiy
ming -v
ming -version
# server功能
ming server
ming server list
ming server add -xx
ming server list
ming server remove -n xxx
ming server list
ming server edit

# 测试local功能
ming local
ming local pc-info
ming local http


time dd if=/dev/zero of=./disk.test bs=4k count=1000000
time dd if=./disk.test of=/dev/null bs=4k


