# !/usr/bin/env python
# -*- coding: utf-8 -*-

#########################
# 定义了对文件的操作    #
#########################

import os


# 该函数传入三个参数，第一个用不到，第二个是当前处理的目录，第三个是当前目录下的文件列表
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
