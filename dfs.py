import collections

class Graph:
	def __init__(self):
		self.graph = {}
	
	def add_edge(self, u, v):
		if u not in self.graph:
			self.graph[u] = []
		if v not in self.graph:
			self.graph[v] = []
		self.graph[u].append(v)
		self.graph[v].append(u)
		
	def bfs(self, start):
		visited = set()
		self._bfs(start, visited)
		
	def _bfs(self,vertex, visited):
		visited.add(vertex)
		print (vertex, end = " ")
		
		for Nei in self.graph[vertex]:
			if Nei not in visited:
				self._bfs(Nei, visited)
graph = Graph()
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(2,5)
graph.add_edge(3,6)
graph.add_edge(3,7)

graph.bfs(1)
	
	
	
	
