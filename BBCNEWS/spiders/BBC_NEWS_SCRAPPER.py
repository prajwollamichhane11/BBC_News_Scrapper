# -*- coding: utf-8 -*-
import scrapy


class BbcNewsScrapperSpider(scrapy.Spider):
    name = 'BBC_NEWS_SCRAPPER'
    allowed_domains = ['www.bbc.com/nepali/news']
    start_urls = ['https://www.bbc.com/nepali/news/']


    def parse(self, response):
        NewsLinks = response.xpath("//div[@class='eagle-item faux-block-link']/div[@class='eagle-item__body']/a/@href").extract()

        NumberOfNews = len(NewsLinks)

        for i in range(NumberOfNews):
            NewsLinks[i] = 'https://www.bbc.com' + NewsLinks[i]

        for link in NewsLinks:
            yield scrapy.Request(link,self.parse_article, dont_filter=True)



    def parse_article(self,response):
        title = response.xpath("//div[@class='column--primary']/div[@class='story-body']/h1/text()").extract()[0]
        article = response.xpath("//div[@class='column--primary']/div[@class='story-body']/div[@class='story-body__inner']/p").extract()

        article_final = ''.join(article)
        yield{
            "News Title":title,
            "News Article":article_final
        }
