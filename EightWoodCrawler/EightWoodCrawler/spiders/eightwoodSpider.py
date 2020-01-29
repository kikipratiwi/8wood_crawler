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
                    url="http://www.8wood.id/pakaian/"+category_text+"/"
                    # The meta is used to send our search text into the parser as metadata
                    yield scrapy.Request(url, callback = self.parse, meta = {"category_text": category_text})



    def parse(self, response):
        """Function to process 8wood category results page"""
        product_category=response.meta["category_text"]
        products=response.xpath("//div[@class='p-list']")
        
        # iterating over search results
        for product in products:
            # Defining the XPaths
            XPATH_PRODUCT_NAME=".//div[@class='desc']//h5/a/text()"
            XPATH_PRODUCT_PRICE=".//div[@class='desc']//div[@class='price-box']//span[@class='regular-price']//span[@class='price']/text()"
            XPATH_PRODUCT_IMAGE_LINK=".//div[@class='img']//a[@class='product-image-custom']//img[contains(@class,'imgThumProduct')]/@data-original"
            XPATH_PRODUCT_LINK=".//div[@class='desc']//h5/a/@href"

            raw_product_name=product.xpath(XPATH_PRODUCT_NAME).extract()
            raw_product_price=product.xpath(XPATH_PRODUCT_PRICE).extract()
            raw_product_image_link=product.xpath(XPATH_PRODUCT_IMAGE_LINK).extract()
            raw_product_link=product.xpath(XPATH_PRODUCT_LINK).extract()
            
            # cleaning the data
            product_name=''.join(raw_product_name).strip(
            ) if raw_product_name else None
            product_price=''.join(raw_product_price).strip(
            ) if raw_product_price else None
            product_image_link=''.join(raw_product_image_link).strip(
            ) if raw_product_image_link else None
            product_link=str(EightwoodspiderSpider.start_urls).join(raw_product_link).strip(
            ) if raw_product_link else None

            yield {
                'product_name': product_name,
                'product_price': product_price,
                'product_link': product_link,
                'image_urls' : raw_product_image_link,
                'images': product_name,
                'category': product_category
            }

        XPATH_PAGINATION_LINK=".//ul[@class='pagination']//li[@class='next']//a/@href"
        raw_pagination_link=response.xpath(XPATH_PAGINATION_LINK).extract()
        pagination_link=''.join(raw_pagination_link).strip(
        ) if raw_pagination_link else None

        next_page = pagination_link
        next_url = 'http://www.8wood.id' + next_page

        if next_page is not None:
            print('logging'+next_url)
            yield response.follow(next_url, callback = self.start_requests)
