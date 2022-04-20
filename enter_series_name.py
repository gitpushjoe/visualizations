import pandas as pd
from mgc_helpers import readtxt, save_to_file, read_from_file
import keyboard
from os import system
from wikipedia_web_scrape import grab_wiki_data
import time

if __name__ == '__main__':
    def input_series_names(): #A script to input what the actual name of a series is based on the name of the film.
        last_shortening = ("", "")
        wiki_df = grab_wiki_data()
        series_names = []
        for i, game in enumerate(wiki_df["Title"]):
            print(f'{last_shortening[0]} → {last_shortening[1]}')
            print(f'\033[1m\033[96m{game}:\033[0m')
            suggested = [game]
            if game.startswith('The ') and game.endswith(' Movie'):
                suggested.append(game.replace('The ','').replace(' Movie','').strip())
                suggested.append(game.replace(' Movie','').strip())
            else:
                if ":" in game:
                    suggested.append(game[:game.find(':')].strip())
                    suggested.append(game[game.find(':')+1:].strip())
            suggested.append('\x1B[3mManual Entry')
            for i, g in enumerate(suggested):
                print(f'\t\033[94m[{i}] {suggested[i]}')
            in_loop = True
            kbkey = None
            while in_loop:
                kbkey = keyboard.read_key()
                if kbkey in [str(n) for n in range(len(suggested))]:
                    kbkey = int(kbkey)
                    print(kbkey)
                    if kbkey != len(suggested) - 1:
                        series_names.append(suggested[kbkey])
                    else:
                        name = input('\t > ')
                        series_names.append(name)
                    in_loop = False
            time.sleep(0.25)
            last_shortening = (game, series_names[-1])
            print("\n\n\n\n\n")
        wiki_df['Series'] = series_names
        save_to_file(wiki_df, "wiki_database.pickle")

    #some formatting
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)
    print(read_from_file("wiki_database.pickle")[:44])
    print(set(read_from_file("wiki_database.pickle")[:44]["Series"].tolist()))
    print(len(set(read_from_file("wiki_database.pickle")[:44]["Series"].tolist())))
    save_to_file(read_from_file("wiki_database.pickle")[:44], "wiki_database_cleaned.pickle")