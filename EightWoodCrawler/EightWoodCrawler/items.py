# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EightwoodcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    ProductTitle    = scrapy.Field()
    ProductCode     = scrapy.Field()
    ProductCategory = scrapy.Field()
    ImageUrl        = scrapy.Field()
    OriginalPrice   = scrapy.Field()
    DetailPageUrl   = scrapy.Field()
    pass
