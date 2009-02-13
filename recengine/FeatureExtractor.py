import re

PROPER_NAME = re.compile("((?:[A-Z][a-z]+ )+(?:[A-Z][a-z]+))")
OPENING_WORDS = re.compile("^(Although|What|The|From|Thus|By|In|Any|Most|If|As|But)\s*")

class FeatureExtractor(object):
    def proper_names(self,text):
        names = PROPER_NAME.findall(text)
        found = []
        if names != None:
            for g in names:
                g = OPENING_WORDS.sub("",g)
                if g.find(" ") > 0:
                    found.append(g)
        return found       
            