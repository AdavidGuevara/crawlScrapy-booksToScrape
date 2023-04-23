from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import Book


class AllBooksSpider(CrawlSpider):
    name = "all_books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/category/books_1/index.html"]
    # custom_settings = {
    #     "FEED_URI": "books.csv",
    #     "FEED_FORMAT": "csv",
    #     "FEED_EXPORT_ENCODING": "utf-8",
    # }

    rules = (
        Rule(LinkExtractor(restrict_css="h3 > a"), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_css=".next > a"), follow=True)
    )

    def parse_item(self, response):
        item = ItemLoader(Book(), response)
        item.add_css('title', 'h1 ::text')
        item.add_xpath('category', '//ul[@class="breadcrumb"]/li[last()-1]/a/text()')
        item.add_xpath('price', '//div[@class="row"]/div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()')
        yield item.load_item()
