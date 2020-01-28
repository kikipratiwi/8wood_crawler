# -*- coding: utf-8 -*-
import scrapy


class EightwoodspiderSpider(scrapy.Spider):
    name = 'eightwoodSpider'
    allowed_domains = ['https://www.8wood.id/pakaian/atasan_wanita/']
    start_urls = ['http://https://www.8wood.id/pakaian/atasan_wanita//']

    def parse(self, response):
        pass
