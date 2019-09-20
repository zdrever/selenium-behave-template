import os
import json

settings = None


class Settings(object):
    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testsettings.json')) as f:
            settings = json.load(f)
            self.url = settings['url']
            self.browser = settings['browser']
            self.driver_timeout = int(settings['driver_timeout'])


settings = Settings()
