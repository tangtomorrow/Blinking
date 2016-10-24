# !/usr/bin/env python
# -*- coding: utf-8 -*-

#########################
# 程序执行入口    		#
#########################

import os

import config
import fileop


def main():
    # step1	遍历数据目录，删除不包含有效数据的文件
    # os.path.walk(config.rootdir, fileop.deleteEmptyFile, ())

    # step2	遍历数据目录，将文件头部两行文字删除
    # os.path.walk(config.rootdir, fileop.deleteTopNLines, 2)

    # step3 将txt文件转换成csv
    os.path.walk(config.rootdir, fileop.convertTxtToCsv, ())

    print 'hello'


main()
