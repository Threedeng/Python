from scrapy.spiders import Spider
from scrapy.selector import Selector
import sys
sys.path.append('E:\Study\Python\Three\Spider\Scrapy\Example\Website\dirbot')
from items import Website
import xlrd
from xlutils.copy import copy
import os

currentdir=os.path.split(os.path.realpath(__file__))[0]


def insertExcel(rowx, colx, content):
    rbook = xlrd.open_workbook(currentdir + '\\result.xlsx')
    wbook = copy(rbook)
    wsheet = wbook.get_sheet(0)
    wsheet.write(rowx, colx, content)
    wbook.save('result.xlsx')

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    ]



    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sites = response.css('#site-list-content > div.site-item > div.title-and-desc')
        items = []
        row = 1
        for site in sites:
            item = Website()
            item['name'] = site.css(
                'a > div.site-title::text').extract_first().strip()
            item['url'] = site.xpath(
                'a/@href').extract_first().strip()
            item['description'] = site.css(
                'div.site-descr::text').extract_first().strip()
            items.append(item)
            print '------------Here is the item:--------------'
            print item["name"]
            print item["url"]
            print item["description"]
            print '----------------over-----------------'
            currentdir=os.path.split(os.path.realpath(__file__))[0]
            print currentdir
            insertExcel(row,0,item['name'])
            insertExcel(row,1,item['url'])
            insertExcel(row,2,item['description'])
            row=row+1


        return items
