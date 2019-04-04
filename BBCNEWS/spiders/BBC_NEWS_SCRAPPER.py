# -*- coding: utf-8 -*-
import scrapy


class BbcNewsScrapperSpider(scrapy.Spider):
    name = 'BBC_NEWS_SCRAPPER'
    allowed_domains = ['https://www.bbc.com/nepali/news']
    start_urls = ['http://https://www.bbc.com/nepali/news/']

    def parse(self, response):
        NewsLinks = response.xpath("//div[@class='eagle-item faux-block-link']/div[@class='eagle-item__body']/a/@href").extract()

        for link in NewsLinks:
            link = 'https://www.bbc.com' + link
            n = yield scrapy.Request(link,self.parse_article)

    def parse_article(self,response):
        NewsTitle = response.xpath('//div[@class="story-body"]/h1/text()').extract()[0]
        NewsBody = response.xpath('//div[@class="story-body__inner"]/p/text()').extract()

        FinalNews = ''.join(NewsBody)
        yield{
            "News Title":NewsTitle,
            "News Article":FinalNews
        }
