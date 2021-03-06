# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YatraOffersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    offer_title = scrapy.Field()
    offer_coupon = scrapy.Field()
    offer_validity = scrapy.Field()
    offer_image = scrapy.Field()
   
    pass