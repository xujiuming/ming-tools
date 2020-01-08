#!/bin/bash
# author ming
# 测试脚本 测试工具是否完善
ming
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