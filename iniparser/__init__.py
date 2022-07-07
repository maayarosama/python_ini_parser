# flake8: noqa

from configparser import ConfigParser
from fcntl import FASYNC
from pickle import FALSE, TRUE
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
        lines= self.content.splitlines()
   
        
        # while True:
        for line in lines:
            # nl = stri.readline()
            
            # if nl == '': break
         
            regex = r"\[([A-Za-z0-9_]+)\]"

            text_inside_paranthesis = re.match(regex, line)
            rx = re.compile(r'(?P<key>\w+)\s*=\s*(?P<value>.+)')
            
            if not line.strip():
                continue

            if text_inside_paranthesis:
                
                dict_name=text_inside_paranthesis.group(1)
                self.d[dict_name]={}
            else:

                params = {
                        match.group('key'):match.group('value')
                        for match in rx.finditer(line)
                        }
                for key, value in params.items():
                    
                    self.d[dict_name][key] = value
            
  
    def to_dict(self):
        print(self.d)
        return self.d


    def get_section(self,sectionname):
        print(self.d[sectionname])
        return self.d[sectionname]
        
    def get_key(self,sectionname,key):
        print(self.d[sectionname][key])
        return self.d[sectionname][key]
    
    # def set_key(self,sectionname,key,newkey):

    #     self.d[sectionname][newkey] = self.d[sectionname].pop[key] 
    #     return self.d[sectionname][newkey] 
   


    def validstr(self):
        stri = StringIO(self.content)
        lines= self.content.splitlines()
        open_list = ["[","{","("]
        close_list = ["]","}",")"]
        stack = []
        balanced="balanced"
        unbalanced="unbalanced"
        for line in lines:

            for i in line:
                if not line.strip():
                    continue
                
                if i in open_list:
                    stack.append(i)
                    
                elif i in close_list:
                    pos = close_list.index(i)
                    if ((len(stack) > 0) and
                        (open_list[pos] == stack[len(stack)-1])):
                        stack.pop()
                    else:
                        return unbalanced
                        
            if len(stack) == 0:
                return balanced
            else:
                return unbalanced
    
        
    def __str__(self):
        str= ""
        for i in self.d:
            str +="["+i+"]\n"
            for j in self.d[i]:
                str += j+" = "+ self.d[i][j] +"\n"
        
        return f'{str}'
    