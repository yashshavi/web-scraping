# -*- coding: utf-8 -*-
import scrapy
class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    site_url = input('enter url\n')
    start_urls = [
        site_url,
    ]
	

    def parse(self, response):
        yield {
		    'page': response.request.url,
			'content': response.css("p::text").extract(),
			'text':response.css("span.text::text").extract()
        }
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
        else:
          page = response.css("footer a::attr(href)").extract_first()
          yield scrapy.Request(response.urljoin(page))    