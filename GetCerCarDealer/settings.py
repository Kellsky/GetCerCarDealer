# -*- coding: utf-8 -*-

# Scrapy settings for GetCerCarDealer project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'GetCerCarDealer'

SPIDER_MODULES = ['GetCerCarDealer.spiders']
NEWSPIDER_MODULE = 'GetCerCarDealer.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'GetCerCarDealer (+http://www.yourdomain.com)'
ITEM_PIPELINES = {'GetCerCarDealer.pipelines.GetcercardealerPipeline':500}