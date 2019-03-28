# -*- coding: utf-8 -*-
import scrapy


class BbcNewsScrapperSpider(scrapy.Spider):
    name = 'BBC_NEWS_SCRAPPER'
    allowed_domains = ['https://www.bbc.com/nepali/news']
    start_urls = ['http://https://www.bbc.com/nepali/news/']

    def parse(self, response):
        NewsLinks = response.xpath('//div[@class="eagle-item__body"]/a/@href').extract()
        pass
