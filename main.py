# !/usr/bin/env python
# -*- coding: utf-8 -*-

#########################
# 程序执行入口    		#
#########################

import os
import sys

import config
import fileop

reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    # step1 读取坐标文件
    places = fileop.readPlaces(config.placesPath)
    print places

    # step2 预处理数据文件
    # step2.1 依照坐标文件中的地点名，将无坐标的文件删除
    os.path.walk(config.rootdir, fileop.deleteNoLatitudFile, places)
    # step2.2	遍历数据目录，删除不包含有效数据的文件
    # os.path.walk(config.rootdir, fileop.deleteEmptyFile, ())
    # step2.3	遍历数据目录，将文件头部两行文字删除
    # os.path.walk(config.rootdir, fileop.deleteTopNLines, 2)
    # step2.4 将txt文件转换成csv
    # os.path.walk(config.rootdir, fileop.convertTxtToCsv, ())

    print 'hello'


main()
