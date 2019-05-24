# -*- coding: utf-8 -*-
 
# Importing Scrapy Library
import scrapy
 
# Creating a new class to implement Spider
class AmazonReviewsSpider(scrapy.Spider):
     
    # Spider name
    name = 'amazon_review'
     
    # Domain names to scrape
    allowed_domains = ['amazon.in']
     
    # Base URL for the MacBook air reviews
    myBaseUrl = "https://www.amazon.in/OnePlus-Midnight-Black-128GB-Storage/product-reviews/B07DJHY82F/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&reviewerType=avp_only_reviews&pageNumber="
    start_urls=[]
    
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,121):
        start_urls.append(myBaseUrl+str(i))
    
    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#cm_cr-review_list')
             
            # Collecting product star ratings
            star_rating = data.css('.review-rating')
             
            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0
             
            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1