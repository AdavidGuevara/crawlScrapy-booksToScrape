import scrapy


class Book(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
