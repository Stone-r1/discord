import requests
from time import sleep
import json

my_list = ["🎶I'm never gonna dance again", "🎶Guilty feet have got no rhythm",
           "🎶Though it's easy to pretend", "🎶I know you're not a fool", "🎶I should've known better", 
           "🎶than to cheat a friend", "🎶And waste the chance", "🎶that I've been given", "🎶So I'm never gonna dance again", 
           "🎶The way I danced with you"]
while True:
    for i in my_list:
        payload = {
            'custom_status': {'text': i}
        }
        header = {
            'authorization': 'your authorization',
            'content-type': 'application/json',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        r = requests.patch('https://discord.com/api/v9/users/@me/settings', data=json.dumps(payload), headers=header)
        sleep(3)