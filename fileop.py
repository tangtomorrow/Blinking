# !/usr/bin/env python
# -*- coding: utf-8 -*-

#########################
# 定义了对文件的操作    #
#########################

import codecs
import os
import re
import sys

import config

reload(sys)
sys.setdefaultencoding('utf-8')


# 该函数传入三个参数，第一个为坐标结果，第二个是当前处理的目录，第三个是当前目录下的文件列表
# 删除当前目录下的无数据文件
def deleteNoLatitudFile(places, dirname, files):
    for file in files:
        # 获取文件的绝对路径
        abspath = os.path.join(dirname, file)

        if os.path.isfile(abspath):
            (filename, extension) = os.path.splitext(file)
            filename = filename[0:-1]

            # 如果文件名（地点名）没有对应的坐标，则删除该文件
            if not places.get(filename):
                os.remove(abspath)


# 该函数传入三个参数，第一个用不到，第二个是当前处理的目录，第三个是当前目录下的文件列表
# 删除当前目录下的无数据文件
def deleteEmptyFile(arg, dirname, files):
    for file in files:
        # 获取文件的绝对路径
        abspath = os.path.join(dirname, file)

        # 定义一个list，用于存放待删除的文件路径名
        filesToBeDeleted = []

        if os.path.isfile(abspath):
            with open(abspath, 'r') as f:
                if len(f.readlines()) <= 2:
                    # 文件行数不大于2，表示该文件没有有效数据，需要加入待删除列表
                    filesToBeDeleted.append(abspath)

            # 删除无效文件
            for fileToBeDeleted in filesToBeDeleted:
                os.remove(fileToBeDeleted)


# 该函数传入三个参数，第一个是需要从首部删除的行数，第二个是当前处理的目录，第三个是当前目录下的文件列表
# 删除当前目录下所有文件的前N行
def deleteTopNLines(numbers, dirname, files):
    for file in files:
        # 获取文件的绝对路径
        abspath = os.path.join(dirname, file)

        if os.path.isfile(abspath):
            with open(abspath, 'r') as f:
                lines = f.readlines()

            # 删除前{numbers}行
            lines = lines[numbers:len(lines)]

            with open(abspath, 'w') as f:
                for line in lines:
                    f.write(line.strip() + '\n')


# 该函数传入三个参数，第一个用不到，第二个是当前处理的目录，第三个是当前目录下的文件列表
def convertTxtToCsv(args, dirname, files):
    for file in files:
        abspath = os.path.join(dirname, file)

        if os.path.isfile(abspath):
            with open(abspath, 'r') as f:
                lines = f.readlines()

            newlines = [config.csvtitle]
            for line in lines:
                newlines.append(convertLine(line))

            # write new line
            str = os.path.splitext(abspath)
            newAbsPath = str[0].replace(config.rootdir, config.rootdirCsv) + ".csv"
            with open(newAbsPath, 'a') as f:
                for line in newlines:
                    f.write(line.strip() + '\n')


# 该函数传入一个参数，将txt中的某一行转换成csv中的某一行
def convertLine(line):
    newLine = ''

    # 处理三位以上数据自带分隔符的问题
    line = line.replace(',', '')

    p = re.compile(r'\s+')
    strs = p.split(line)

    temperatureIndex = strs[1].index(':00:00') + 6
    time = strs[0] + '' + strs[1][0:temperatureIndex]
    temperature = strs[1][temperatureIndex:len(strs[1])]
    strs[0] = time
    strs[1] = temperature

    for s in strs:
        if s == "-":
            newLine += ','
        else:
            newLine += s
            newLine += ','

    return newLine


# 根据locations.txt，读取地点名和对应的两个坐标，并存入字典，字典中key对应地点名，value对应坐标
def readPlaces(placesPath, fileEncoding='utf-8'):
    places = dict()
    with codecs.open(placesPath, 'r', fileEncoding) as f:
        lines = f.readlines()
        for line in lines:
            strs = line.split(" ", 1)
            # print strs[0], "------", strs[1]
            # print type(strs[0])
            places[strs[0]] = strs[1]
    return places
