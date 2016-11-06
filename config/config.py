# coding: utf-8
import json
import requests

class Config:

    def __init__(self):
        with open('config.json') as file:
            self.config = json.load(file)

    def updateConfig(self):
        r = requests.get(url=self.config['updateurl'])
        self.config = json.loads(r.text)
        with open('config.json', 'w') as file:
            json.dump(self.config, file)
        return self.config
