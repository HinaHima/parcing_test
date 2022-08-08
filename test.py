import json

with open('best_games.json', 'r') as f:
    data = json.load(f)
    game = []
    for game_name in data.keys():
        game.append(game_name)
    games_list = []

    games = data['Games']
    lenght = len(data['Games'])
    count = 0

    while count < lenght:
        games_list.append(games[count])
        count += 1

print(f'{game[0]}: {games_list}')

