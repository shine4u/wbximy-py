# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Response
from scrapy.http import Request

class DoubanMovieAllSpider(scrapy.Spider):
    name = 'douban_movie_all'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20']

    def parse(self, response: Response):
        self.logger.debug("a=%s", response.text)

        request = Request(

        )
