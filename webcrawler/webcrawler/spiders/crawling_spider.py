from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = "crawling_spider"
    allowed_domains =["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    rules =(
        Rule(LinkExtractor(allow="catalogue/category")),
    )