import scrapy


class PokemonSpider(scrapy.Spider):
    name = 'pokemon'
    allowed_domains = ['yakkun.com']
    start_urls = ['http://yakkun.com/']

    def parse(self, response):
        pass
