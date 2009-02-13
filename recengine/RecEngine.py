#coding=utf8

ALL = 1
import pickle

from heapq import nlargest
from operator import itemgetter

RELATED_LIST = 1
ADJACENCY_LIST = 2

class RecEngine(object):

    people = {}
    items  = {}
    
    def __init__(self):
        pass
        
    def add(self,p,item):
        if not self.people.has_key(p):
            self.people[p] = set()
        self.people[p].add(item)   
       
    def build(self,alpha=0.5,num_similar=10):
        items = {}
        print "building..."
        # make a frequency table of all items
        for p in self.people.values():
            for elem in p:
                if items.has_key(elem):
                    items[elem][0] += 1
                else:
                    items[elem] = [0,[],[]]
                    
        self.items = items  
        
        # pre-calculate an adjacency list of people for each item
        for i in self.items.keys():
            for pkey,itemlist in self.people.iteritems():
                if i in itemlist:
                    self.items[i][ADJACENCY_LIST].append(pkey)
         
        # calculate similarity scores against other items and store the top N
        for i in self.items.keys():
            scores = {}
            for j in self.items.keys():  
                if i == j: continue
                cp = self.cond_prob(i,j)
                if cp == 0:
                    continue
                scores[j] = cp
                
            top =  nlargest(num_similar, scores.iteritems(), itemgetter(1))  
            self.items[i][RELATED_LIST] = top
                    
            
                
    def stats(self):
        return { 'nodes' : '' }
        
        
    def run(self):
        pass
            
    
    def xxsimilar_items(self,basket):
        n = 20
        for item in basket:
            toplist = find_similar(self,item,n)
            scores = normalize(toplist)
            
 
    def find_similar(self,item):
        nearby = self.items[item][1]
        return nearby
            
    def similar_users(self,person):
        for p in self.people:
            pass
            
    def cond_prob(self,u,v,alpha=0.5):
        """
        formula used here is 
            F(u|v) 
        -------------------
        F(v) * (F(u))^alpha
        
        Where alpha is a domain specific constant between zero and one
        """
        left  = len(self.items[u][ADJACENCY_LIST])
        right = len(self.items[v][ADJACENCY_LIST])
        both  = len(filter(lambda x:x in self.items[u][ADJACENCY_LIST],
                                         self.items[v][ADJACENCY_LIST]))
        if left  == 0: return None
        if right == 0: return None
        if both  == 0: return 0
        return float(both) / ( float(left) * pow(right,alpha))
        
def normalize(list):
    """
    Given a list of id,score tuples, add the scores and normalize so they sum
    to unit length
    """
    sum = 0
    for id,score in list:
        sum += score
    for id,score in list:
        scaled = float(score)/float(sum)
        norm.append((id,scaled))
    return norm
    
    
if __name__=='__main__':
    print "testing"
    re = RecEngine()
    v1 = [0,2,0,0,2,9,0,0,0,4,0]
    v2 = [1,0,0,0,3,0,0,2,0,0,0]
    
    people = {
        'p1' : [ 'He', 'Ne', 'O', 'C', 'U'],
        'p2' : [ 'H', 'O', 'Cl'],
        'p3' : [ 'N', 'S', 'U' ],
        'p4' : [ 'Se', 'F', 'O' ],
        'p5' : [ 'H', 'O' ]
    }
    for p,vec in people.iteritems():
        for v in vec:
            re.add(p,v)
    re.build()
    cp = re.cond_prob("H", "O")
    
    print str(cp)
   # both = 2
   # left = 2
   # right = 4
   # den = 4
   # expect 0.471
   # cp = cond_prob(v1,v2)
   # print str(cp)
    
        