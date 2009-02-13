#coding=utf8
from HTMLParser import HTMLParser
import re

class Parser(HTMLParser):
    on = False
    lines = []
    
    def parse(self,path):
        file = open(path)
        lines = file.readlines()
        txt = "".join(lines)
        return self.parse_string(txt)
    
    def parse_string(self,str):
        self.reset()
        self.lines = []
        self.on = False
        self.feed(str)
        self.close()
        text = "".join(self.lines)
        rx = re.compile("[\s\n]+")
        text = rx.sub(" ", text)
        return text
        
    def handle_entityref(self,name):
        if self.on == False: return
        if name == "quot":
            self.lines.append('"')
        else:
            self.lines.append("**" + name)
    
    def handle_charref(self,num):
        if self.on == False: return
        if num == "39":
            self.lines.append("'")
        elif num == "233":
            self.lines.append("é")
        else:
            self.lines.append("##" + num)
            
    def handle_starttag(self,tag,attrs):
        if tag == 'p':
            self.on = True
        pass
    
    def handle_endtag(self,tag):
        if tag == 'p':
            self.on = False
        pass
        
    def handle_data(self,data):
        if self.on:
            self.lines.append(data)
        pass
        


if __name__ == '__main__':
    import sys
    path = sys.argv[1]
    p = Parser()
    print p.parse(path)