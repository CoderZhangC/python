# -*- coding: utf-8 -*-
import scrapy
import json
import random


class CaixukunSpider(scrapy.Spider):
    

    def start_requests(self):  # 以start_requests代替strat_urls启动爬虫
        name = 'caixukun'
        allowed_domains = ['quotes.toscrape.com']
        urls = ['http://quotes.toscrape.com/']  # 该链接通过浏览器抓包得来（微博移动端）
        

    def parse(self, response):  # 解析函数
        quotes = response.css('.quote')
        for quote in quotes:
            item = Quoteitem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            print(item)
            yield item
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        join(next)
        yield scrapy.Request(url=url, callback=self.parse)