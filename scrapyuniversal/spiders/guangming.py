# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.items import ScrapyuniversalItem

class GuangmingSpider(CrawlSpider):
    name = 'guangming'
    # allowed_domains = ['politics.gmw.cn']
    # start_urls = [
    #     'http://politics.gmw.cn/node_9840.htm',
    #     'http://politics.gmw.cn/node_9844.htm',
    #     'http://politics.gmw.cn/node_103380.htm',
    #     'http://politics.gmw.cn/node_9831.htm',
    #     'http://politics.gmw.cn/node_9828.htm',
    #     'http://politics.gmw.cn/node_9826.htm',
    #     'http://politics.gmw.cn/node_9833.htm'
    # ]
    #
    # rules = (
    #     Rule(LinkExtractor(allow=r'2020.*/.*/content_.*.htm', restrict_xpaths='//ul[@class="channel-newsGroup"]'), callback='parse_item'),
    #     Rule(LinkExtractor(restrict_xpaths='//div[@id="displaypagenum"]//a[contains(.,  "下一页")]'))
    # )

    allowed_domains = [
            'gmw.cn',
                       ]

    start_urls = [
        'http://www.gmw.cn/',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'\w+.gmv.cn'),
             follow=True),
        Rule(LinkExtractor(allow=r'node_\d+.htm'),follow=True),
        Rule(LinkExtractor(allow=r'2020.*/.*/content_.*.htm'),callback='parse_item')
    )

    def parse_item(self, response):
        item = ScrapyuniversalItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        Title =  ('').join(response.xpath('//h1[@class="u-title"]/text()').extract_first())
        Content = ('').join(response.xpath('//div[@class="u-mainText"]//text()').extract())
        item['Title'] = Title.strip()
        item['Content'] = Content.strip().replace('\n','').replace('\t','').replace('\r','').replace('\u3000','').replace(' ','')
        yield item


    # def parse_item(self, response):
    #     item = ScrapyuniversalItem()
    #     #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
    #     #i['name'] = response.xpath('//div[@id="name"]').extract()
    #     #i['description'] = response.xpath('//div[@id="description"]').extract()
    #     Title =  ('').join(response.xpath('//h1[@class="u-title"]/text()').extract_first())
    #     Content = ('').join(response.xpath('//div[@class="u-mainText"]//text()').extract())
    #     item['Title'] = Title.strip()
    #     item['Content'] = Content.strip().replace('\n','').replace('\t','').replace('\r','').replace('\u3000','').replace(' ','')
    #     yield item
