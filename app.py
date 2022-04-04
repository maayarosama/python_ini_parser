# flake8: noqa

from configparser import ConfigParser

class IniParser:
    # def __init__(self):
        


    def read(self,x, y):
        config= ConfigParser()
        config.read('configs.ini')
        print(config[x][y])




# print(config['database']['host'])
