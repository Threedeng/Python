#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test1.py


class test():
    global sum
    sum = 'Hello,I am global!'
    def printhellow(self):
        print ("I am print hellow Python")
        print (sum)



tst = test()
tst.printhellow()
