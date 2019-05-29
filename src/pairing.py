import json
import requests
import slackapi
import time

slackapi._auth()

try:
    with open('pairings.json', 'r') as db:
        pairings = json.load(db)
except FileNotFoundError:
    pairings = []

while True:
    answer = input('(P) Pairing (E) Submit (S) Skip:\n')
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
    elif answer.upper() == 'E':
        with open('pairings.json', 'w') as db:
            json.dump(pairings, db)
    elif answer.upper() == 'S':
		with open('pairings.json', 'w') as db:
    json.dump(pairings, db)
		break
    else:
        print('huh ? Try again !')

channels_creator = input('Do i create channels for the players ? Yes or No ?')
if channels_creator.upper() == 'YES':
    try:
        for i in range(100):
            white_p = pairings[i]['white_player']
            black_p = pairings[i]['black_player']
            white_tz = slackapi.get_utc(pairings[i]['white_tz'])
            time.sleep(1)
            black_tz = slackapi.get_utc(pairings[i]['black_tz'])
            message = f'You have been paired in BlindFold #3 Round 1.\n'\
                      + f'<@{white_p}> (_white pieces_ , {white_tz}) vs <@{black_p}> (_black pieces_, {black_tz}) @ 15+10\n'\
                      + 'Message your opponent here as soon as possible.\n'\
                      + 'When you have agreed on a time, post it in <#CFD0VEV7G|blindfold-scheduling>.\n'
            time.sleep(1)
            slackapi.create_group_dm('%s, %s' % (white_p, black_p))
            channel_id = slackapi.create_group_dm('%s, %s' % (white_p, black_p)
            time.sleep(1)
            slackapi.send_message(message, channel_id)
            if white_p == '<Your ID>':
                slackapi.create_group_dm('%s' % (black_p))
                channel_id = slackapi.create_group_dm('%s, %s' % (white_p, black_p))
                time.sleep(1)
            elif black_p == '<Your ID>':
                slackapi.create_group_dm('%s' % (black_p))
                channel_id = slackapi.create_group_dm('%s, %s' % (white_p, black_p))
                time.sleep(1)
            else:
                slackapi.create_group_dm('%s, %s' % (white_p, black_p))
                channel_id = slackapi.create_group_dm('%s, %s' % (white_p, black_p))
                time.sleep(1)
                slackapi.close_conversation(channel_id)
    except IndexError:
        pass
