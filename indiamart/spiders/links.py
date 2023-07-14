# Run command: scrapy crawl spider1 -o spider1.json

import scrapy
import csv

class Spider1Spider(scrapy.Spider):
    name = "links"
    allowed_domains = ["dir.indiamart.com"]
    start_urls = ["https://dir.indiamart.com/indianexporters/te_fabri.html"]

    def parse(self, response):
        slink = response.css('li.box-new')
        atags = slink.css('a.slink')

        for tag in atags:
            link = tag.attrib['href']
            output_filename = f"links.csv"

            with open(output_filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([link])
