import re
import sys
from recengine.Parser import Parser
from recengine.FeatureExtractor import FeatureExtractor

          
if __name__=="__main__":
    file = sys.argv[1]
    p = Parser()
    text = p.parse(file)
    fe = FeatureExtractor()
    features = fe.proper_names(text)
    for f in features:
        print f