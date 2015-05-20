# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class GetcercardealerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dealer_name = Field()
    dealer_stocks = Field() #number of stocks to sell
    dealer_starrate = Field()
    dealer_ratings = Field()
    dealer_location = Field()
    dealer_distance = Field()
    dealer_phn = Field()
    dealer_moreinfo = Field()
