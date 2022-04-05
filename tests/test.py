# flake8: noqa
import os
import re
# import sys
# sys.path.insert(1, '../src')
# import app

# from INNI_PARSER.src.app import IniParser

# from ../srcpip3 install import app 
from iniparser import IniParser

string ="""" [DEFAULT]
title = Hello world
compression = yes
compression_level = 9

[database]
host = 127.0.0.1
user = username
pass = password
alive = no
"""


    
ini_parse=IniParser("""[DEFAULT]
title = Hello world
compression = yes
compression_level = 9

[database]
host = 127.0.0.1
user = username
pass = password
keep-alive = no

                    """)



def test():
    assert ini_parse.getSectionInfo('database') != ""
    assert ini_parse.getSpecficInfo('database','host') != ""
    assert ini_parse.getAllInfo() != ""

