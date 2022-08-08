import requests
from bs4 import BeautifulSoup
import json

filename = 'best_games.json'

def results():
    print(filename)

def main():
    page = 1
    games = []
    python_dict = {'Games' : []}
    while page <= 19:
        pages_info = requests.get('https://stopgame.ru/games/filter?rating=izumitelno&p=' + str(page))
        data = BeautifulSoup(pages_info.text, 'html.parser')


        each = data.find_all('div', class_ = "caption caption-bold")

        if page <= 19:
            print(f'Parcing games on page {page}...')
            for single in each:
                game_name = single.select('a')[0].get_text()

                games.append(game_name.strip())
            page += 1

    for game in games:
        python_dict['Games'] += [game]

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(python_dict, f)

    print('Parcing finished')


if __name__ == '__main__':
    main()