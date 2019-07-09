# -*- coding: utf-8 -*-
import scrapy
from ..items import YatraOffersItem


class YatraOffersSpider(scrapy.Spider):
    name = 'yatra_offers'
    start_urls = [
    	'https://www.yatra.com/offer/dom/listing/domestic-flight-deals',
    ]

    next_pages = [
		'https://www.yatra.com/offer/dom/listing/international-flight-deals',
		'https://www.yatra.com/offer/dom/listing/domestic-hotel-deals',
		'https://www.yatra.com/offer/dom/listing/holiday-deals',
		'https://www.yatra.com/offer/listing/bus',
		'https://www.yatra.com/offer/listing/activity-deals'
	]
    
    total_pages = 0

    def parse(self, response):
    	items = YatraOffersItem()

    	all_li_offers = response.css('ul.wfull')

    	for offers in all_li_offers:
    		offer_title = offers.css('.offerMainTitle::text').extract()
    		offer_coupon = offers.css('.mt5::text').extract()
    		offer_validity = offers.css('.date::text').extract()
    		offer_image = offers.css('.respnsiv-img::attr(src)').extract()

    		items['offer_title'] = offer_title
	    	items['offer_coupon'] = offer_coupon
	    	items['offer_validity'] = offer_validity
	    	items['offer_image'] = offer_image

	    	yield items

	    	if YatraOffersSpider.total_pages < 5:
	    		YatraOffersSpider.total_pages += 1
	    		yield response.follow(YatraOffersSpider.next_pages[YatraOffersSpider.total_pages], callback = self.parse)
