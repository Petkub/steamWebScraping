import requests
from lxml import html
import csv

def write_to_csv(filename, data):
    with open(filename, 'w', encoding ='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data.keys())
        writer.writerows(zip(*data.values()))

def rogue_lite():
    res = requests.get('https://store.steampowered.com/search/?tags=3959&category1=998&os=win&supportedlang=english', 
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'})
    # print(res.status_code)

    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')
    
    # for i in range(len(game_link)):
    #     print(i+1,": ",game_link[i])

    # for i in range(len(release_date)):
    #     print(i+1,": ",release_date[i])
    
    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Rogue-lite'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}

    # for i in range(40):
    #     print(i + 1 , ": ", game_infomation['Rogue-lite_game'][i], game_infomation['price'][i].strip())

    write_to_csv('csv_file/RogueLite_game.csv', clean_game_infomation)

def rogue_like():
    res = requests.get('https://store.steampowered.com/search/?tags=1716&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Rogue-like'] * len(name)

    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    # print(clean_game_infomation)
    write_to_csv('csv_file/RogueLike_game.csv', clean_game_infomation)

def souls_like():
    res = requests.get('https://store.steampowered.com/search/?tags=29482&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Souls-like'] * len(name)

    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    # for v, k in clean_game_infomation.items():
    #     print(v, k)
    write_to_csv('csv_file/SoulsLike_game.csv', clean_game_infomation)

def adventure():
    res = requests.get('https://store.steampowered.com/search/?tags=21&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Adventure'] * len(name)

    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Adventure_game.csv', clean_game_infomation)

def action():
    res = requests.get('https://store.steampowered.com/search/?tags=1718&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Action'] * len(name)

    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    remove_priceIsNone = {k: [v for v in value if v != ''] for k, value in clean_game_infomation.items()}
    write_to_csv('csv_file/Action_game.csv', clean_game_infomation)

def MOBA():
    res = requests.get('https://store.steampowered.com/search/?tags=1718&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)

    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['MOBA'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    
    
    # write_to_csv('csv_file/MOBA_game.csv', clean_game_infomation)
    write_to_csv('csv_file/MOBA_game1.csv', clean_game_infomation)

def MMO_RPG():
    res = requests.get('https://store.steampowered.com/search/?tags=1754&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['MMO_RPG'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/MMO_RPG_game.csv', clean_game_infomation)

def puzzle():
    res = requests.get('https://store.steampowered.com/search/?tags=1664&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Puzzle'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Puzzle_game.csv', clean_game_infomation)

def tower_defense():
    res = requests.get('https://store.steampowered.com/search/?tags=1645&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Tower Defense'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Tower_Defense_game.csv', clean_game_infomation)

def survival():
    res = requests.get('https://store.steampowered.com/search/?tags=1662&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Survival'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Survival_game.csv', clean_game_infomation)

def simulator():
    res = requests.get('https://store.steampowered.com/search/?tags=599%2C597&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Simulator'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Simulator_game.csv', clean_game_infomation)

def horor():
    res = requests.get('https://store.steampowered.com/search/?tags=1667&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Horor'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Horor_game.csv', clean_game_infomation)

def RTS():
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=1676&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['RTS'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/RTS_game.csv', clean_game_infomation)

def Hack_and_Slash():
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=1646&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Hack and Slash'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Hack_and_Slash_game.csv', clean_game_infomation)

def fighting():
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=1743&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Fighting'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Fighting_game.csv', clean_game_infomation)

def sport():
    res = requests.get('https://store.steampowered.com/search/?tags=701&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Sport'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Sport_game.csv', clean_game_infomation)

def strategy():
    res = requests.get('https://store.steampowered.com/search/?tags=9&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Strategy'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Strategy_game.csv', clean_game_infomation)

def turn_based():
    res = requests.get('https://store.steampowered.com/search/?tags=1677&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Turn Based'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Turn_based_game.csv', clean_game_infomation)

def racing():
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=699&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Racing'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Racing_game.csv', clean_game_infomation)

def arcade():
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=1773&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Arcade'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Arcade_game.csv', clean_game_infomation)

def dating():
    res = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&tags=9551&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Dating'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Dating_game.csv', clean_game_infomation)

def metroidvania():
    res = requests.get('https://store.steampowered.com/search/?tags=1628&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Metroidvania'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Metroidvania_game.csv', clean_game_infomation)

def FPS():
    res = requests.get('https://store.steampowered.com/search/?tags=1663&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['FPS'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/FPS_game.csv', clean_game_infomation)

def card():
    res = requests.get('https://store.steampowered.com/search/?tags=1666&category1=998&os=win&supportedlang=english',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'})
    # print(res.status_code)
    tree = html.fromstring(html=res.text)
    name = tree.xpath('//span[@class="title"]/text()')
    price = tree.xpath("//div[@class = 'col search_price  responsive_secondrow']/text() | //div[@class = 'col search_price discounted responsive_secondrow']/text()[2]")
    game_link = tree.xpath('//a[@class="search_result_row ds_collapse_flag "]/@href')
    release_date = tree.xpath('//div[@class="col search_released responsive_secondrow"]/text()')

    game_infomation = {
        'game': name,
        'price': price,
        'link' : game_link,
        'release_date': release_date,
        'game_type' : ['Card'] * len(name)
    }
    clean_game_infomation = {k: [v.strip() for v in value] for k, value in game_infomation.items()}
    write_to_csv('csv_file/Card_game.csv', clean_game_infomation)

if __name__ == '__main__':
    rogue_lite()
    adventure()
    souls_like()
    action()
    rogue_like()
    MOBA()
    MMO_RPG()
    puzzle()
    tower_defense()
    survival()
    simulator()
    horor()
    RTS()
    Hack_and_Slash()
    fighting()
    sport()
    strategy()
    turn_based()
    racing()
    arcade()
    dating()
    metroidvania()
    FPS()
    card()
