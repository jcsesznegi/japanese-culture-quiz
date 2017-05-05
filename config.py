import sys, os
from configparser import SafeConfigParser

class Config():
    parser      = SafeConfigParser()
    environment = None

    def __init__(self):
        self.parser.read( os.path.dirname( os.path.abspath(__file__) ) + '/config.ini' )
        self.environment = self.parser.get('default', 'environment')

    def get(self, key):
        return self.parser.get(self.environment, key)

config = Config()
