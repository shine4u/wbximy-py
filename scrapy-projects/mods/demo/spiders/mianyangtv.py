# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Response
from scrapy.selector import Selector


class MianyangtvSpider(scrapy.Spider):
    name = 'mianyangtv'
    start_urls = [
        'http://www.myntv.cn/html/zb/jmd.asp',
    ]

    def parse(self, response: Response):
        # self.logger.debug("a=%s", response.text)
        selector = Selector(response=response)
        weekdays = selector.xpath('//div[@class="Contentbox"]/div')
        self.logger.debug('weekdays size=%d', len(weekdays))
        for weekday in weekdays:
            playlist = weekday.xpath('.//div/ul/li')
            for play in playlist:
                play_text = play.attrib.get('vn')
                self.logger.info('play_text=%s', play_text)

