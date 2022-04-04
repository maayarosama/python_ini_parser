# flake8: noqa

from configparser import ConfigParser


config= ConfigParser()
print(config.sections())

config.read('configs.ini')
print(config.sections())

print(config['DEFAULT']['title'])
print(config['database']['host'])
