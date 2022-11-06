import requests
from lxml import html
import csv
import re

def write_to_csv(filename, data):
    with open(filename, 'w', encoding ='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data.keys())
        writer.writerows(zip(*data.values()))

def re_img_link(image):
    for i in range(len(image)):
        image[i] = re.sub(r"(capsule_sm_*[0-9]*[a_-z]*[0-9]*.)", "header.", image[i])
    return image

def re_price(price):
    for i in range(len(price)):
            price[i] = re.sub(r"[\r \n ฿ ,]", "", price[i])
            if(price[i] == 'Free' or price[i] == 'FreeToPlay' or price[i] == 'FreetoPlay'):
                price[i] = 0
    return price

def scraping(res, n, p, link, re_date, img, category):
    tree = html.fromstring(html=res.text)
    name = tree.xpath(n)
    price = tree.xpath(p)
    game_link = tree.xpath(link)
    release_date = tree.xpath(re_date)
    image = tree.xpath(img)
        
    re_img_link(image)
    re_price(price)

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : [category] * len(name),
        'image' : image
    }
    write_to_csv('csv_file/' + category + '_game.csv', game_infomation)
    

def rogue_lite(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=3959&category1=998&os=win&supportedlang=english', 
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'})
    scraping(res, n, p, link, re_date, img, 'Rogue-lite')

    
def rogue_like(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=1716&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Rogue-like')

def souls_like(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=29482&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Souls-like')


def adventure(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=21&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Adventure')

def action(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=4106&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Action')

def MOBA(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=1718&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'MOBA')

def MMO_RPG(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=1754&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'MMO_RPG')

def puzzle(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=1664&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Puzzle')

def tower_defense(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=1645&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Tower Defense')

def survival(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=1662&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Survival')

def simulator(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=599%2C597&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Simulator')

def horor(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=1667&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Horor')

def RTS(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=1676&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'RTS')

def Hack_and_Slash(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=1646&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Hack and Slash')

def fighting(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=1743&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Fighting')

def sport(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=701&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Sport')

def strategy(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=9&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Strategy')

def turn_based(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=1677&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Turn Based')

def racing(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=699&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Racing')

def arcade(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=1773&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Arcade')

def dating(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=9551&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Dating')

def metroidvania(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=1628&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Metroidvania')

def FPS(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=1663&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'FPS')

def card(n, p, link, re_date, img):
    res = requests.get('https://store.steampowered.com/search/?tags=1666&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    scraping(res, n, p, link, re_date, img, 'Card')

if __name__ == '__main__':
    name = '//span[@class="title"]/text()'
    price = "//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]"
    game_link = '//a[@class="search_result_row ds_collapse_flag "]/@href'
    release_date = '//div[@class="col search_released responsive_secondrow"]/text()'
    image = '//div[@class = "col search_capsule"]/img/@src'
    rogue_lite(name, price, game_link, release_date, image)
    rogue_like(name, price, game_link, release_date, image)
    dating(name, price, game_link, release_date, image)
    metroidvania(name, price, game_link, release_date, image)
    FPS(name, price, game_link, release_date, image)
    card(name, price, game_link, release_date, image)
    MOBA(name, price, game_link, release_date, image)
    adventure(name, price, game_link, release_date, image)
    survival(name, price, game_link, release_date, image)
    strategy(name, price, game_link, release_date, image)
    action(name, price, game_link, release_date, image)
    simulator(name, price, game_link, release_date, image)
    MMO_RPG(name, price, game_link, release_date, image)
    Hack_and_Slash(name, price, game_link, release_date, image)
    fighting(name, price, game_link, release_date, image)
    puzzle(name, price, game_link, release_date, image)
    racing(name, price, game_link, release_date, image)
    turn_based(name, price, game_link, release_date, image)
    tower_defense(name, price, game_link, release_date, image)
    arcade(name, price, game_link, release_date, image)
    souls_like(name, price, game_link, release_date, image)
    horor(name, price, game_link, release_date, image)
    sport(name, price, game_link, release_date, image)
    RTS(name, price, game_link, release_date, image)