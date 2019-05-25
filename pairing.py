import json
import requests
import slackapi
slackapi._slack_token()

try:
    with open('pairings.json', 'r') as db:
        pairings = json.load(db)
except FileNotFoundError:
    pairings = []

while True:
    answer = input('(P) Pairing (S) Submit:\n')
    if answer.upper() == 'P':
        round = input('Round: ')
        white_player = input('White Player: ')
        black_player = input('Black Player: ')

        pairings.append({
        'white_player': slackapi._get_user_id(white_player),
        'white_tz': slackapi._get_user_info(slackapi._get_user_id(white_player), 'tz'),
        'black_player': slackapi._get_user_id(black_player),
        'black_tz': slackapi._get_user_info(slackapi._get_user_id(black_player), 'tz')
        })
    elif answer.upper() == 'S':
        break
    else:
        print('huh ? Try again !')
with open('pairings.json', 'w') as db:
    json.dump(pairings, db)
