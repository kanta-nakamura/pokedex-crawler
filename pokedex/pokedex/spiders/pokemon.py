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

        for i, tr in enumerate(response.css('table[summary="基本データ"] tr')):
            if i == 0:
                item['name_ja'] = tr.css('::text').get()
            elif tr.css('::text').get() == '全国No.':
                item['global_id'] = tr.css('::text').getall()[1]
            elif tr.css('::text').get() == 'シンオウNo.':
                item['local_id'] = tr.css('::text').getall()[1]
            elif tr.css('::text').get() == '高さ':
                item['height'] = tr.css('::text').getall()[1]
            elif tr.css('::text').get() == '重さ':
                item['weight'] = tr.css('::text').getall()[1]
            elif tr.css('::text').get() == '英語名':
                item['name_en'] = tr.css('::text').getall()[1]
            elif tr.css('::text').get() == 'タイプ':
                item['type1'] = tr.css('img')[0].attrib['alt']
                try:
                    item['type2'] = tr.css('img')[1].attrib['alt']
                except IndexError:
                    item['type2'] = None

        item['bs_hp'] = response.css('table[summary="詳細データ"] tr')[1].css('td::text').getall()[1].strip()
        item['bs_atk'] = response.css('table[summary="詳細データ"] tr')[2].css('td::text').getall()[1].strip()
        item['bs_def'] = response.css('table[summary="詳細データ"] tr')[3].css('td::text').getall()[1].strip()
        item['bs_satk'] = response.css('table[summary="詳細データ"] tr')[4].css('td::text').getall()[1].strip()
        item['bs_sdef'] = response.css('table[summary="詳細データ"] tr')[5].css('td::text').getall()[1].strip()
        item['bs_spd'] = response.css('table[summary="詳細データ"] tr')[6].css('td::text').getall()[1].strip()

        yield item
