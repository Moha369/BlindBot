import re

def get_id(url):
    iden = re.findall('/lichess4545.slack.com/messages/([A-Z0-9])/$', url)
    print(iden)

get_id('https://lichess4545.slack.com/messages/G0DFRURGQ/details/')
