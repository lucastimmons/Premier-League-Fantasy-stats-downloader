import requests
import json

all_players = {}
playerurl = "http://fantasy.premierleague.com/web/api/elements/%s/"
# don't know the full range, 577 was the highest when i went to 700 but i guess that could change
for i in range(577):    
    playerget = requests.get(playerurl % i)
    if playerget.status_code != 200: 
	continue
    all_players[i] = playerget.json()

with open('all_the_players.json', 'w') as outfile:
  json.dump(all_players, outfile)