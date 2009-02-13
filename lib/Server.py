
class Server(object):
    qp = None
    def __init__(self):
        self.qp = QueryParser()
        
    def query(self,query):
        try:
            query = self.qp.parse(raw)
        except Exception, e:
            print "fail"
            
       
            
   