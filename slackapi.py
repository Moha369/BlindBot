import requests
import json

def _slack_token():
    slack_token = '<SLACK_TOKEN>'
    return slack_token

def _get_user_id(user_name):
    with open('slack_identities.json', 'r') as si:
        slack_identities = json.load(si)
    try:
        for i in range(100):
            id = slack_identities[i]['slack_name']
            if id == user_name:
                return slack_identities[i]['slack_id']
    except:
        pass
def _get_user_info(userID, info):
    url = 'https://slack.com/api/users.info'
    r = requests.get(url, params={"token": _slack_token(), 'user': userID})
    res = r.json()
    return res['user'][info]
def create_group_dm(users):
    r = requests.post("https://slack.com/api/conversations.open", params={'token': _slack_token(),'return_im': True, 'users': users, 'as_user': True})
    res = r.json()
    return(res['channel']['id'])

def invite_to_group_dm(group_id, user_id):
    url = 'https://api.slack.com/methods/conversations.invite'
    r = requests.post(url, params={'token': _slack_token(), 'channel': group_id, 'users': user_id})
    res = r.json()
    return res
def send_message(message, dm_id):
    url = 'https://slack.com/api/chat.postMessage'
    r = requests.post(url, params={'token': _slack_token(), 'channel': dm_id, 'text': message})
    print(r.status_code)
