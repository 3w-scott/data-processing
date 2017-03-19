#!/usr/bin/python
# -*- coding: UTF-8 -*-
# http://blog.csdn.net/keenweiwei/article/details/9037727
# http://www.myexception.cn/operating-system/1977513.html
import os

# 只输出files，而不是用for循环，就会导致只输出了根目录下的文件夹和文件
# root,dirs,files=os.walk("D:\study\python\python文档", topdown=False)
file_object1 = open('hydrophobic.txt', 'w')
for root, dirs, files in os.walk("D:\study\数据挖掘&&生物信息\hydrophobic", topdown=True):
    for name in files:
        # 对于每一个文件的操作：
        file_object = open(os.path.join(root, name))
        lines = file_object.readlines()
        file_object1.write(name)
        result = list()
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.strip()
            # print(line[4])
            if (line[4] in {'A', 'C', 'G', 'U'} and line[5].isdigit()):
                index = line.index(':')
                # print(result)

                result.append(line[index + 1] + ':' + line[4:index])
        file_object1.write('%s' % '\n'.join(result))
        if (result):
            file_object1.write('%s' % '\n')  # 在每个文件最后输入一个空行
file_object.close()
file_object1.close()

file_objcet2 = open('hbond.txt', 'w+')

for root, dirs, files in os.walk("D:\study\数据挖掘&&生物信息\Hbond", topdown=True):
    for name in files:
        # 对于每一个文件的操作：
        file_object = open(os.path.join(root, name))
        lines = file_object.readlines()
        file_objcet2.write(name)
        result = list()
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.strip()
            # print(line[4])
            if (line[0] in {'A', 'C', 'G', 'U'}):
                index = line.index(':')
                # print(result)

                result.append(line[index + 1] + ':' + line[:index])
        file_objcet2.write('%s' % '\n'.join(result))
        if (result):
            file_objcet2.write('%s' % '\n')  # 在每个文件最后输入一个空行
file_object.close()
file_object1.close()
