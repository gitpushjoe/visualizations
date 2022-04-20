import pandas as pd
from bs4 import BeautifulSoup
from mgc_helpers import readtxt, save_to_file, read_from_file


def grab_wiki_data():
    wiki_data = readtxt('wikipedia_table.txt', return_str=False, rem_comment=True)
    wiki_data = ''.join(wiki_data)
    df = pd.read_html(wiki_data)
    df = pd.DataFrame(df[0])
    for i, game in enumerate(df['Title']):
        if '[' in game:
            df['Title'][i] = game[:game.find('[')]
    return df

def append_animated_movies():
    wiki_data = readtxt('wikipedia_animated_table.txt', return_str=False, rem_comment=True)
    wiki_data = ''.join(wiki_data)
    df = pd.read_html(wiki_data)
    df = pd.DataFrame(df[0])
    for i, game in enumerate(df['Title']):
        if '[' in game:
            df['Title'][i] = game[:game.find('[')]
    return df

# wikidf = read_from_file('film_and_game_data.pickle')
# print(wikidf, wikidf.axes)
#
# angrybirds = {'Series': 'Angry Birds',
#                'Top Game': 'Angry Birds Rio HD',
#                'Game Rating': '88',
#                'Game URL': '/game/ios/angry-birds-rio-hd',
#                'Game Platform': 'iOS',
#                'Game Year': '2011'
#                }
#
# finalfantasytsw = {'Title': 'Final Fantasy: The Spirits Within',
#                    'Series': 'Final Fantasy',
#                    'Top Game': 'Final Fantasy IX',
#                    'Game Rating': '94',
#                    'Game URL': '/game/playstation/final-fantasy-ix',
#                    'Game Platform': 'PS',
#                    'Game Year': '2000'
#                    }
#
# ratchetandclank = {'Title': 'Ratchet & Clank',
#                    'Series': 'Ratchet & Clank',
#                    'Top Game': 'Ratchet & Clank: Up Your Arsenal',
#                    'Game Rating': '91',
#                    'Game URL': '/game/playstation-2/ratchet-clank-up-your-arsenal',
#                    'Game Platform': 'PS2',
#                    'Game Year': '2004'
#                    }
#
# wikidf = wikidf.to_dict(orient='index')
# wikidf[44].update(finalfantasytsw)
# wikidf[45].update(ratchetandclank)
# wikidf[46].update(angrybirds)
# wikidf[47].update(angrybirds)
# wikidf = pd.DataFrame.from_dict(wikidf, orient='index').astype(str)
# pd.set_option('display.max_columns', None)
# save_to_file(wikidf, 'film_and_game_data_01.pickle')
# print(wikidf[['Title', 'Release date', 'Series', 'Game Rating', 'Game Platform','Game Year']])

wikidf = read_from_file('film_and_game_data_01.pickle')
wikidf.to_csv('data.csv')