# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokedexItem(scrapy.Item):
    '''
    ポケモン図鑑に記載する項目を定義
    '''
    
    global_id = scrapy.Field()  # 全国No.
    local_id = scrapy.Field()  # 地方No.
    name_ja = scrapy.Field()  # ポケモン日本語名
    name_en = scrapy.Field()  # ポケモン英語名
    height = scrapy.Field()  # 高さ
    weight = scrapy.Field()  # 重さ
    type1 = scrapy.Field()  # タイプ1
    type2 = scrapy.Field()  # タイプ2
    bs_hp = scrapy.Field()  # 種族値(HP)
    bs_atk = scrapy.Field()  # 種族値(こうげき)
    bs_def = scrapy.Field()  # 種族値(ぼうぎょ)
    bs_satk = scrapy.Field()  # 種族値(とくこう)
    bs_sdef = scrapy.Field()  # 種族値(とくぼう)
    bs_spd = scrapy.Field()  # 種族値(すばやさ)