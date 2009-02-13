import os
import sys
import time
from subprocess import Popen, PIPE
from recengine.Parser import Parser
from recengine.FeatureExtractor import FeatureExtractor
from recengine.RecEngine import RecEngine
import pickle

def read(path):
    parser = Parser()
    print "> entered read " + path
    todo = []
    for dir, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullname = os.path.join(dir, file)
            if file.endswith(".gz"):
                todo.append(fullname)
    total = len(todo)
    print "found " + str(total) + " files to process"
    count = 0
    fe = FeatureExtractor()
    rec = RecEngine()
    
    for file in todo:
        text = None
        pipe = Popen(["gunzip", "-c", file], stdout=PIPE)
        pipe.wait()
        count += 1
        out,err = pipe.communicate()
        print "parsing  (" + str(count) + "/" + str(total) + ")  " + file 
        try:
            parsed = parser.parse_string(out)
        except:
            continue
        names = fe.proper_names(parsed)
       # print parsed
        for n in names:
            rec.add(n,file)
           # print "  " + n
        #print parsed
    rec.build()
    f = open("pickled.dat","w")
    pickle.dump(rec,f)

    
if __name__ == '__main__':
    
    try:
        path = sys.argv[1]
    except:
        print "usage: parse_articles.py DIR"
    read(path)