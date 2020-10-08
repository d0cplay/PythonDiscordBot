import json

def config():
    with open('./bot/config.json') as f: #load config
        return(json.load(f))