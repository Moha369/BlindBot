# BlindBot
BlindBot is made for a blindfold league to help the moderators in the repetitve tasks

# What does this Bot Do ?
* This bot is designed to work on a chess league, you have to configure the [Databse](https://github.com/Moha369/BlindBot/blob/master/database.py) by running it and assign every player or user ID in slack., it will save this data in a JSON File called _slack_identities_
* You can now run the [JSON Extractor](https://github.com/Moha369/BlindBot/blob/master/json_extract.py) so you can check everything is ok.
* Now run the [Pairings](https://github.com/Moha369/BlindBot/blob/master/pairing.py) app and assign the white and black players, it will also save them to json file called _pairings.json_

# Instructions
* Whenever you want to add a new player, just run database.py and add him, do not play with slack_identities.json otherwise it will not open again and you have to delete it so database.py can work again
* Whenever you want to add a new pairing, just run pairing.py and add it, do not play with pairings.json otherwise it will not open again and you have to delete it so pairing.py can work again
* Follow the instructions of each program, you will find it in comments inside the program and while running it

# Requirements
* In [Slack API File](https://github.com/Moha369/BlindBot/blob/master/slackapi.py#L5) change the `<SLACK_TOKEN>` to the token you will get from slack when you make your bot.
* JSON library ```pip install json``` **Note**: _It might be installed already_
* Requests Library ```pip install requests```
