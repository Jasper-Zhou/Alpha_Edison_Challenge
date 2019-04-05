import scrapy
from patient.items import PatientItem
import re
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PatientDiscussionSpider(scrapy.Spider):
    name = 'PatientDiscussion'
    allowed_domains = ['patient.info']

    def __init__(self):
        self.file = open('PatientDiscussion.jl','a')
        self.numOfExpectedPages = 20
        self.page_count = 0
        self.temp_dict = {}

    def start_requests(self):
        # start from the target page
        start_urls = ['https://patient.info/forums/discuss/browse/abdominal-disorders-3321']
        
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        self.page_count += 1
        if self.page_count > self.numOfExpectedPages:
            return

        # follow links to other pages
        for href in response.css("a[rel='discussion'][title='View replies']::attr(href)").extract():
            complet_href = "https://patient.info" + href
            yield scrapy.Request(complet_href, callback=self.disscusion_parse)
            
        # next redirect
        nextPageUrl = response.css("link[rel='next'] ::attr(href)").extract_first()
        yield scrapy.Request(nextPageUrl, callback=self.parse)

    def disscusion_parse(self, response): 
        if response.url.find("patient.info/forums/discuss/") != -1:
            item = PatientItem() 
            # content id
            content_id = response.css("meta[property='og:url']::attr(content)").extract()[0][-6:]
            item['content_id'] = content_id 

            # writer part
            writer = response.css("div[class='author'] h5[class='author__info'] a::text").extract()[0]
            post = response.xpath("//div[@id='post_content'][@class='post__content']//text()").extract()
            post_content =  "".join(line.strip() for line in post[:-21])
            post_timestamp  = response.css("div[id='topic'][class='post__main'] p[class='post__stats'] time[class='fuzzy']::attr(datetime)").extract_first()
            dict_post = {'writer':writer, 'post_content':post_content, 'post_timestamp':post_timestamp}
            item['post'] = dict_post
            
            # replies part
            dict_reply = {}
            reply = response.css("ul[class='comments'] li[class='comment'] article[class='post post__root']")
            for i in range(len(reply)):
                responsers = reply[i].css("div[class='post__header'] h5[class='author__info'] a[rel='author']::text").extract_first()
                response_time = reply[i].css("div[class='post__header'] p[class='post__stats'] time[class='fuzzy']::attr(datetime)").extract_first()
                response_text = "".join(reply[i].xpath("div[@class='post__content break-word'][@itemprop='text']//text()").extract()[:-21]).strip().replace('\r\n','')[:]
                dict_reply[i] = {'responser':responsers, 'response_time':response_time, 'response_text':response_text}
            item['reply'] = dict_reply

            # next reply page
            nextPageUrl = response.css("a[class='reply__control reply-ctrl-last link']::attr(href)").extract_first()
            if nextPageUrl != None:
                yield scrapy.Request(nextPageUrl, callback=self.disscusion_parse)
            self.file.write(json.dumps(dict(item))+ '\n') 

 