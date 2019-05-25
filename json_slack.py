import json
import sys

with open('slack_identities.json', 'r') as si:
    slack_identities = json.load(si)

for i in range(100):
    try:
        print('The player %s slack id is (%s) and timezone is %s' % (slack_identities[i]['slack_name'], slack_identities[i]['slack_id'], slack_identities[i]['tz']))
    except IndexError:
        pass
