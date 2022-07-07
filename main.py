# flake8: noqa



from iniparser import IniParser

    
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


ini_parse.get_key('database','host')
ini_parse.to_dict()