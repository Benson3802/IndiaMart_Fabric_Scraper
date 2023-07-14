# Run command: scrapy crawl spider1 -o spider1.json

import scrapy

class Spider1Spider(scrapy.Spider):
    name = "spider1"
    allowed_domains = ["dir.indiamart.com"]
    #get start urls from links.csv

    start_urls = []
    with open('links.csv', 'r') as f:
        for line in f:
            start_urls.append("https://dir.indiamart.com/"+line.strip())


    def parse(self, response):
        products = response.css("div.l-cl.b-w")
        sellers = response.css("div.r-cl.b-gry")

        for product, seller in zip(products, sellers):
            try:
                yield {
                    'productname': product.css('h3::text').get(),
                    'price': product.css('span.prc.cur::text').get().replace('₹\xa0', '').replace('/', ''),
                    'productlink': product.css('a.read.wh.mlin').attrib['href'],
                    'sellername': seller.css('h2::text').get(),
                    'phnumber': seller.css('span.pns_h.duet::text').get(),
                    'address': seller.css('span.to-txt::text').get().strip(),
                    'sellerlink': seller.css('a').attrib['href'],
                }
            except:
                yield {
                    'productname': product.css('h3::text').get(),
                    'price': 'Not available',
                    'productlink': 'Not available',
                    'sellername': seller.css('h3::text').get(),
                    'phnumber': seller.css('span.pns_h.duet::text').get(),
                    'address': seller.css('span.to-txt::text').get().strip(),
                    'sellerlink': 'Not available',
                }
