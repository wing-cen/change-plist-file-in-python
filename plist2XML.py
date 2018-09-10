"""
Author: WING
Date:   20180806
Use:    To change many plist file's version in one time and return xml type file
"""

def getType(value):
    if isinstance(value, int):
        if isinstance(value, bool):
            return 'bool'
        return 'integer'
    elif isinstance(value, bytes):
        try:
            buff = value.decode('utf-8')
            txt = 'stringa'
        except:
            try:
                buff = value.decode('utf-16')
                txt = 'stringb'
            except:
                pass
        return txt
    elif isinstance(value, str):
        return 'string'
    elif isinstance(value, list):
        return 'array'
    elif isinstance(value, dict):
        return 'dict'
    else:
        return 'Error Type:' + str(type(value))


# 转成str型，比较方便后面使用
def toStr(key):
    keytype = getType(key)
    if keytype == 'stringa':
        return key.decode('utf-8')
    elif keytype == 'stringb':
        return key.decode('utf-16')
    elif keytype == 'string':
        # 声明全局变量
        global strID
        global strDict

        strDict[strID] = key
        strID = strID + 1
        # return str.format('%04d' % (strID - 1))
        return key
    elif keytype == 'integer':
        return str(key)

    elif keytype == 'bool':
        if key == True:
            return 'true'
        else:
            return 'false'
    else:
        return 'Unknow Type Return!'


# 字典转字符
def dict2str(dictx):
    global gtab

    buff = ''
    buff = buff + '<dict>\n'

    gtab = gtab + 1
    tabs = getTabs()

    for key in dictx:
        buff = buff + tabs + '<key>' + toStr(key) + '</key>\n'
        buff = buff + tabs

        value = dictx[key]
        valuetype = getType(value)
        if valuetype == 'dict':
            buff = buff + dict2str(value)
        elif valuetype == 'array':
            buff = buff + list2str(value)
        elif valuetype == 'bool':
            buff = buff + '<' + toStr(value) + '/>\n'
        else:
            if valuetype == 'stringa' or valuetype == 'stringb':
                valuetype = 'string'
            buff = buff + '<' + valuetype + '>' + toStr(value) + '</' + valuetype + '>\n'

    gtab = gtab - 1
    tabs = getTabs()

    buff = buff + tabs
    buff = buff + '</dict>\n'
    return buff


# 列表在plist的xml格式里为array
def list2str(listx):
    global gtab

    buff = ''
    tabs = getTabs()
    buff = buff + tabs + '<array>\n'

    gtab = gtab + 1

    for value in listx:
        valuetype = getType(value)
        if valuetype == 'dict':
            buff = buff + dict2str(value)
        elif valuetype == 'array':
            buff = buff + list2str(value)
        else:
            print('list ')
    gtab = gtab - 1
    tabs = getTabs()

    buff = buff + tabs + '</array>\n'
    return buff


# 缩进距离，排版xml
def getTabs():
    buff = ''
    for i in range(gtab):
        buff = buff + '\t'
    return buff

def exportPlist(fn):
    plist = biplist.readPlist(fn)
    plist["CFBundleShortVersionString"] = fileVersion
    plist["WebPluginDescription"] = fileVersion
    mineTypeStr = list(plist["WebPluginMIMETypes"])[0]
    plist["WebPluginMIMETypes"][mineTypeStr]["WebPluginTypeDescription"] = fileVersion
    buff = dict2str(plist)
    fp = open(fn[:-5] + 'plist', 'w', encoding='utf-8')

    temp = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">\n'''
    fp.write(temp)
    fp.write(buff)
    fp.write('</plist>')
    fp.close()


if __name__ == '__main__':
    import glob
    import os
    import biplist

    gtab = 0
    strID = 0
    strDict = {}
    files = glob.glob('*.plist')
    fileVersion = ''
    fileVersion = input("Please Input Version:")

    for fn in files:
        if os.path.isfile(fn):
            exportPlist(fn)
            print(fn + "   has changed.")
