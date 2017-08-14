# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RfItem(scrapy.Item):
    # define the fields for your item here like:
    URL = scrapy.Field()
    Address = scrapy.Field()
    Id = scrapy.Field()
    Compensation = scrapy.Field()
    Area = scrapy.Field()
    Date_time = scrapy.Field()
    Gig_Type = scrapy.Field()
    Description = scrapy.Field()
