from bs4 import BeautifulSoup
import urllib3
import requests
from mgc_helpers import readtxt, save_to_file, read_from_file
import pandas as pd
import time
import random


class Game:
    HEADER = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    META_PRE = 'https://www.metacritic.com/search/all/'
    META_SUF = '/results?sort=score'

    def __init__(self, title, platform, year, score, url, series):
        self.title = title
        self.platform = platform
        self.year = year
        self.score = score
        self.url = url
        self.series = series

    def meta_search(series_name):
        url = Game.META_PRE + series_name.lower().replace(' ', '%20') + Game.META_SUF
        s = requests.Session()
        s.headers['User-Agent'] = Game.HEADER
        r = s.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        g = soup.find('ul', {'class': 'search_results module'}).find_all('li')[0]
        results = {}
        results['title'] = g.find('a').contents[0].replace('\n', '').strip()
        results['url'] = g.find('a')['href']
        results['platform'] = g.find('span', {'class': 'platform'}).contents[0].strip()
        year = str(g.find('p'))
        year = year[year.find("Game, ") + 5:year.find("Game, ") + 10].strip()
        results['year'] = year
        try:
            results['score'] = g.find('span', {'class': 'metascore_w medium game positive'}).contents[0].strip()
        except AttributeError:
            results['score'] = g.find('span', {'class': 'metascore_w medium game mixed'}).contents[0].strip()
        except AttributeError:
            results['score'] = g.find('span', {'class': 'metascore_w medium game negative'}).contents[0].strip()
        results['series'] = series_name
        return Game(title=results['title'],
                    url=results['url'],
                    platform=results['platform'],
                    score=results['score'],
                    year=results['year'],
                    series=results['series'])

if __name__ == '__main__':
    # wikidata = read_from_file("wiki_database_cleaned.pickle")
    # print(wikidata)
    # titles, urls, plats, scores, years = list(), list(), list(), list(), list()
    # top_games_of_series = {}
    # for series in wikidata['Series']:
    #     game = top_games_of_series.setdefault(series, Game.meta_search(series))
    #     titles.append(game.title)
    #     urls.append(game.url)
    #     plats.append(game.platform)
    #     scores.append(game.score)
    #     years.append(game.year)
    #     print(f'{game.series:<22} {game.title}, {game.year}: {scores[-1]}')
    #     time.sleep(1)
    # wikidata["Top Game"] = titles
    # wikidata["Game Rating"] = scores
    # wikidata["Game URL"] = urls
    # wikidata["Game Platform"] = plats
    # wikidata["Game Year"] = years
    # print(wikidata)
    # save_to_file(wikidata, "film_and_game_data.pickle")
    print(read_from_file('film_and_game_data.pickle')[['Metacritic', 'Top Game', 'Game Rating']])

    #Game.meta_search(series_name="super mario bros.")