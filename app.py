import requests
from lxml import html
import csv

def write_to_csv(filename, data):
    with open(filename, 'w', encoding ='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data.keys())
        writer.writerows(zip(*data.values()))

def rogue_lite():
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=3959&category1=998&os=win', 
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'})
    # print(res.status_code)

    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")

    game_infomation = {
        'Rogue-lite_game': name,
        'price': price
    }
    strip_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}

    # for i in range(40):
    #     print(i + 1 , ": ", game_infomation['Rogue-lite_game'][i], game_infomation['price'][i].strip())

    # write_to_csv('game.csv', strip_game_infomation)

if __name__ == '__main__':
    rogue_lite()