from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pokedex.items import PokedexItem


class PokemonSpider(CrawlSpider):
    name = 'pokemon'
    allowed_domains = ['yakkun.com']
    start_urls = ['https://yakkun.com/bdsp/zukan/']

    rules = (
        Rule(LinkExtractor(allow=r'/bdsp/zukan/n\d+$'), callback='parse_stats'),  # 特殊フォルムはクローリング対象外
    )

    def parse_stats(self, response):
        '''
        ポケモンのデータを抜き出す。
        '''

        item = PokedexItem()
        item['global_id'] = response.css('table[summary="基本データ"] tr')[3].css('td::text').getall()[1]
        item['local_id'] = response.css('table[summary="基本データ"] tr')[4].css('td::text').getall()[1]
        item['name_ja'] = response.css('table[summary="基本データ"] tr')[0].css('th::text').get()
        item['name_en'] = response.css('table[summary="基本データ"] tr')[8].css('li::text').get()
        item['height'] = response.css('table[summary="基本データ"] tr')[5].css('td::text').getall()[1]
        item['weight'] = response.css('table[summary="基本データ"] tr')[6].css('li::text').getall()[0]
        item['type1'] = response.css('table[summary="基本データ"] tr')[7].css('img')[0].attrib['alt']
        try:
            item['type2'] = response.css('table[summary="基本データ"] tr')[7].css('img')[1].attrib['alt']
        except IndexError:  # 複合タイプでない場合
            item['type2'] = None
        item['bs_hp'] = response.css('table[summary="詳細データ"] tr')[1].css('td::text').getall()[1].strip()
        item['bs_atk'] = response.css('table[summary="詳細データ"] tr')[2].css('td::text').getall()[1].strip()
        item['bs_def'] = response.css('table[summary="詳細データ"] tr')[3].css('td::text').getall()[1].strip()
        item['bs_satk'] = response.css('table[summary="詳細データ"] tr')[4].css('td::text').getall()[1].strip()
        item['bs_sdef'] = response.css('table[summary="詳細データ"] tr')[5].css('td::text').getall()[1].strip()
        item['bs_spd'] = response.css('table[summary="詳細データ"] tr')[6].css('td::text').getall()[1].strip()

        yield item
