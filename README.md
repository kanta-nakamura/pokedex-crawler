# pokedex-crawler

ポケモンのデータ（bdspのみ）を取得するクローラー<br>
取得先：https://yakkun.com/

## 実行方法
```
$ scrapy crawl pokemon -o output.csv
```
```
$ head output.csv
bs_atk,bs_def,bs_hp,bs_satk,bs_sdef,bs_spd,global_id,height,local_id,name_en,name_ja,type1,type2,weight
68,64,55,45,55,31,387,0.4m,001,Turtwig,ナエトル,くさ,,10.2kg
30,30,60,36,56,50,163,0.7m,106,Hoothoot,ホーホー,ノーマル,ひこう,21.2kg
90,55,60,90,80,110,026,0.8m,105,Raichu,ライチュウ,でんき,,30.0kg
55,40,35,50,50,90,025,0.4m,104,Pikachu,ピカチュウ,でんき,,6.0kg
```
## 取得対象項目
|変数名|項目名|
|---|---|
|global_id|全国No.|
|local_id|地方No.|
|name_ja|ポケモン日本語名|
|name_en|ポケモン英語名|
|height|高さ|
|weight|重さ|
|type1|タイプ1|
|type2|タイプ2|
|bs_hp|種族値(HP)|
|bs_atk|種族値(こうげき)|
|bs_def|種族値(ぼうぎょ)|
|bs_satk|種族値(とくこう)|
|bs_sdef|種族値(とくぼう)|
|bs_spd|種族値(すばやさ)|
