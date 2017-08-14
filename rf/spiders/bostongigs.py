# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from time import sleep
import random

class BostongigsSpider(scrapy.Spider):
    name = 'bostongigs'
    def __init__(self,location='',*args,**kwargs):
        super(BostongigsSpider,self).__init__(*args,**kwargs)
        self.allowed_domains = ['boston.craigslist.org']
        self.start_urls = ['https://boston.craigslist.org/search/'+location +'/ggg']

    def parse(self, response):

        gigs = response.xpath('//p[@class="result-info"]')
        for gig in gigs:
            relative_url = gig.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
            title = gig.xpath('a/text()').extract_first()
            address = gig.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
            yield Request(absolute_url, callback=self.parse_page, meta={'URL': absolute_url, 'Title': title, 'Address':address})
        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = "https://boston.craigslist.org" + relative_next_url
        yield Request(absolute_next_url, callback=self.parse)

    def parse_page(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        address = response.meta.get('Address')
        postid = response.xpath('//div[2]/p[1]/text()').extract_first().split('post id: ')[1]
        compensation = response.xpath('//p[@class="attrgroup"]/span[1]/b/text()').extract_first()
        city = response.xpath('//small/text()').extract_first()
        area = response.xpath('//li[2]/p/a/text()').extract_first()
        date_time = response.xpath('//*[@id="display-date"]/time/text()').extract_first()
        gig_type = response.xpath('//li[4]/p/a/text()').extract_first()
        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract()).replace('\n','')

        yield{'URL': url,
            'Title': title,
            'Address': address,
            'Id': postid,
            'Compensation': compensation,
            'Area': area,
            'Date_time': date_time,
            'Gig_Type': gig_type,
            'Description': description
            }

        sleep(random.randrange(15,30))
