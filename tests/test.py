# flake8: noqa

from app import IniParser

ini_parse=IniParser()

def test():
   assert ini_parse.read('database','host')
