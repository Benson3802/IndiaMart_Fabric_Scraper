# IndiaMart_Fabric_Scraper
Use Scrapy to scrape all product description listed as 'fabrics'

## 1	Objective
The objective of this assignment is to extract product and seller details related to fabrics from IndiaMart. 

> **Note**
> While scraping data from websites, ensure that you are legally allowed to do so by complying with the *robots.txt* file. Contact the owner of the website for details on what you can or cannot do. 

## Prerequisites
The following libraries are required to run the code. Use the following commands to install the libraries.

### Pandas
> ### conda
> 
> conda install pandas
>
> ### or PyPI
> 
> pip install pandas

### Scrapy
> ### conda
> 
> conda install -c conda-forge scrapy
>
> ### or PyPI
> 
> pip install Scrapy

## [Scrapy Documentation](https://docs.scrapy.org/en/latest/)


### Open the terminal in the main directory of the project and run these commands


#### To download the required URLs for scraping
>
> Scrapy crawl links


#### To scrape data from the URLs
>
> scrapy crawl spider1 -O <filename><.json>/<.csv>

