# flake8: noqa
# import os
# import sys
# sys.path.insert(1, '../src')
# import app

# from INNI_PARSER.src.app import IniParser

# from ../srcpip3 install import app 
from app import IniParser

ini_parse=IniParser()

def test():
    assert ini_parse.read('database','host') != ""
