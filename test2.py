# -*- coding: utf-8 -*-
import urllib2
from scrapy.spiders import Spider

from test1 import printhellow

def transSalary(salary):
    result = ''
    if "千" in salary:
        begnum = float(salary.split("-")[0]) * 1000
        endnum = float(salary.split('-')[1].split('千')[0]) * 1000
    elif "万" in salary:
        begnum = float(salary.split("-")[0]) * 10000
        endnum = float(salary.split('-')[1].split('万')[0]) * 10000
    else:
        return "No wan or qian"

    if '年' in salary:
        begnum = begnum/12
        endnum = endnum/12

    result = str(begnum) + '-' + str(endnum)
    return result,begnum,endnum


salary = '3-5千'

print transSalary(salary)





