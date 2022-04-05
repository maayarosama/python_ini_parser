# flake8: noqa

from configparser import ConfigParser
import re

from io import StringIO

class IniParser:
    d={}
    def __init__(self,content):
        self.content=content
        self.Parsing()
      
        

    def getsections(self):
        
        s=re.findall(r"\[([A-Za-z0-9_]+)\]", self.content)

        print(s)
        
 
    def Parsing(self):
        stri = StringIO(self.content)
   
        
        while True:
            nl = stri.readline()
            if nl == '': break
         
            regex = r"\[([A-Za-z0-9_]+)\]"

            text_inside_paranthesis = re.match(regex, nl)
            rx = re.compile(r'(?P<key>\w+)\s*=\s*(?P<value>.+)')

            if text_inside_paranthesis:
                
                dict_name=text_inside_paranthesis.group(1)
                self.d[dict_name]={}
            else:

                params = {
                        match.group('key'):match.group('value')
                        for match in rx.finditer(nl)
                        }
                for key, value in params.items():
                    
                    self.d[dict_name][key] = value
                    
  
    def getAllInfo(self):
        print(self.d)

    def getSectionInfo(self,sectionname):
        print(self.d[sectionname])
        
    def getSpecficInfo(self,sectionname,info):
        print(self.d[sectionname][info])
              


            
            
            
    def dict(self):
        d = {}

        size = 5
        for i in range(size):
            
            dict_name = input("Enter the name of child dictionary: ")
            d[dict_name] = {}
            Name = input("Enter name: ")
            Age = input("Enter Age: ")
            d[dict_name]["Name"] = Name
            d[dict_name]["Age"] = Age
            
        print(d)
            
    # def read(self,x, y):
    #     config= ConfigParser()
    #     config.read(self.content)
    #     print(config[x][y])




