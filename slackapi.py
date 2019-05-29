import requests
import json

def _auth():
    slack_token =
    return slack_token

def _get_user_id(user_name):
    with open('slack_identities.json', 'r') as si:
        slack_identities = json.load(si)
    try:
        for i in range(100):
            id = slack_identities[i]['slack_name']
            if id == user_name:
                return slack_identities[i]['slack_id']
    except IndexError:
        pass

def _get_user_info(userID, info):
    url = 'https://slack.com/api/users.info'
    r = requests.get(url, params={"token": _auth(), 'user': userID})
    res = r.json()
    return res['user'][info]

def create_group_dm(users):
    r = requests.post("https://slack.com/api/conversations.open", params={'token': _auth(),'return_im': True, 'users': users})
    res = r.json()
    return(res['channel']['id'])

def invite_to_group_dm(group_id, user_id):
    url = 'https://api.slack.com/methods/conversations.invite'
    r = requests.post(url, params={'token': _auth(), 'channel': group_id, 'users': user_id})
    res = r.json()
    return res

def send_message(message, dm_id):
    url = 'https://slack.com/api/chat.postMessage'
    r = requests.post(url, params={'token': _auth(), 'channel': dm_id, 'text': message, 'as_user': 'true'})
    res = r.json()
    print(res['ok'])

def close_conversation(channel):
    url = 'https://slack.com/api/conversations.close'
    r = requests.post(url, params={'token': _auth(), 'channel': channel})

def get_utc(zone):
    r = requests.get('https://api.timezonedb.com/v2.1/list-time-zone', params={'key': <Your Key>, 'format': 'json', 'zone': zone, 'fields': 'gmtOffset'})
    final = r.json()['zones'][0]['gmtOffset'] /60/60
    final = int(final)
    if final >= 0:
        return (f"UTC+{final}")
    else:
        return f"UTC-{final}"
