from Node 	 import *
from NodeSet import *
class Query:
	
	_nodes 		= None
	_maskNodes 	= None
	_type  		= None
	_limit 		= None
	
	QUERY 		 = "query"
	INTERSECTION = "intersection"
	
	DEFAULT_LIMIT = 15
	DEFAULT_TYPE  = QUERY
	
	def __init__(self,nset):
		assert isinstance(nset, NodeSet)
		self._nodes = nset
		self._maskNodes = NodeSet()
		self._type = self.DEFAULT_TYPE
		self._limit = {}
		for type in Node.TYPES:
			self._limit[type] = self.DEFAULT_LIMIT
	
	def canonicalize(self):
		nodeList = [ n.toString() for n in self._nodes ]
		nodeList.sort()
		nodes = ",".join(nodeList)
		
		
		maskList = [ (n.toString() + ":" + "".join(n.mask()) ) for n in self._maskNodes ]
		maskList.sort()
		
		limitList = [ n + ":" + str(self.limit(n)) for n in Node.TYPES ]
		limitList.sort()
		
		return "ask{" + nodes + "} " \
				+ "mask{" + ",".join(maskList) + "} " \
				+ "type{" + self._type + "}" \
				+ " limit{" + ",".join(limitList) + "}"
		
		
	def nodeCount(self):
		return self._nodes.count()
		
	def nodes(self):
		 return self._nodes
	
	def maskNodes(self):
		return self._maskNodes
	
	def polygonNodes(self):
		out = []
		for n in self._nodes:
			if n.type() == Node.POLYGON:
				out.append(n)
		return out
		
	def type(self):
		return self._type
		
	def limit(self,type=None):
		if type == None:
			return self._limit	
		else:
			return self._limit[type]
		
	def setMaskNodes(self,nodes):
		assert isinstance(nodes, NodeSet)
		self._maskNodes = nodes
		
	def dump(self):
		for n in self._nodes:
			print n.toString()
	
	def setLimit(self, lim, type = None):
		if type == None:
			for t in Node.TYPES:
				self._limit[t] = lim
		else:
			self._limit[type] = lim
		
	def setType(self, type):
		self._type = type
	

		
