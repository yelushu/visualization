#! /usr/bin/env python
#-*- encoding: utf-8 -*-


import os
import sys
from MainlyGui.MainApp import MainApp

# os.path.abspath('.') 表示当前所处的文件夹的绝对路径
# os.walk 函数返回遍历的目录、文件夹列表、文件列表
for root, dirs, files in os.walk(os.path.abspath('.')):
    #print(root, dirs, files)
    sys.path.append(root) # 添加到环境变量中

if __name__ == '__main__':

    app = MainApp()
    app.MainLoop()


