"""
Author: WING
Date:   20180806
Use:    To change many plist file's version in one time and return binary type file
"""

import os
from biplist import *


if __name__ == '__main__':
    fileVersion = input("please input version:") #get workspace path
    filePath = os.path.dirname(os.path.realpath(__file__))
    files = []
    dirs = os.listdir(filePath)

    for i in dirs:  # 循环读取路径下的文件并筛选输出
        if os.path.splitext(i)[1] == ".plist":  # 筛选plist文件
            files.append(i)
    for ff in files:
        try:
            plist = readPlist(filePath+"/"+ff)
            plist["CFBundleShortVersionString"] = fileVersion
            plist["WebPluginDescription"] = fileVersion
            mineTypeStr = list(plist["WebPluginMIMETypes"])[0]
            plist["WebPluginMIMETypes"][mineTypeStr]["WebPluginTypeDescription"] = fileVersion
            writePlist(plist,ff)
            print(ff+"   has changed.")
        except:
            pass

