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




#Split into different functions
def test_sections():
    assert ini_parse.get_section('database') == {'host': '127.0.0.1', 'user': 'username', 'pass': 'password', 'alive': 'no'}
    assert ini_parse.get_section('DEFAULT') ==     {'title': 'Hello world', 'compression': 'yes', 'compression_level': '9'}


def test_key():
    assert ini_parse.get_key('database','host') == "127.0.0.1"
    assert ini_parse.get_key('database','user') == "username"
    assert ini_parse.get_key('database','pass') == "password"
    assert ini_parse.get_key('database','alive') == "no"



    
    
def test_dict():
    assert ini_parse.to_dict() == {'DEFAULT': {'title': 'Hello world', 'compression': 'yes', 'compression_level': '9'}, 'database': {'host': '127.0.0.1', 'user': 'username', 'pass': 'password', 'alive': 'no'}}

def test_str():
    assert str(ini_parse) != ''
    
def test_validate_str():
    assert ini_parse.validstr() == "balanced"


    