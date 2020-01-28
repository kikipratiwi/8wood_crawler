# -*- coding: utf-8 -*-
import scrapy
import csv
import os


class EightwoodspiderSpider(scrapy.Spider):
    name = 'eightwoodSpider'
    allowed_domains = ['8wood.id']
    start_urls = ['http://www.8wood.id/']

    def start_requests(self):
            """Read category_text from categories file amd construct the URL"""

            with open(os.path.join(os.path.dirname(__file__), "../resources/categories.csv")) as categories:
                for category in csv.DictReader(categories):
                    category_text=category["category"]
                    url="http://www.8wood.id/pakaian/".format(
                        category_text)
                    # The meta is used to send our search text into the parser as metadata
                    yield scrapy.Request(url, callback = self.parse, meta = {"category_text": category_text})



    def parse(self, response):
        """Function to process 8wood category results page"""
        product_category=response.meta["category_text"]
        products=response.xpath("//div[@class='p-list']")
        

            


