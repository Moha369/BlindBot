import json
import requests
import slackapi

try:
    with open('slack_identities.json', 'r') as db:
        slack_profiles = json.load(db)
except FileNotFoundError:
    slack_profiles = []

while True:
    answer = input('List new pairing (L) Import entries (W)')
    if answer.upper() == 'NEW PAIRINGS' or answer.upper() == 'L':
        slack_name = input('Slack Name: ')
        slack_id = input('ID: ')

        slack_profiles.append({
            'slack_name': slack_name,
            'slack_id': slack_id,
            'tz': slackapi._get_user_info(slack_id)
            })
    elif answer.upper() == 'IMPORT ENTRIES' or answer.upper() == 'W':
        break

with open('slack_identities.json', 'w') as db:
    json.dump(slack_profiles, db)
