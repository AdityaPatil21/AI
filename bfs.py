from collections import deque

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
        queue = deque([start])  # Use a deque as the queue for BFS traversal
        self._bfs(queue, visited)

    def _bfs(self, queue, visited):
        if not queue:  # Base case: the queue is empty
            return
        
        vertex = queue.popleft()  # Dequeue the vertex from the left side of the queue
        visited.add(vertex)  # Mark the current vertex as visited
        print(vertex, end=" ")  # Print the visited vertex
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)  # Enqueue the neighbor vertex
        
        self._bfs(queue, visited)  # Recursive call to process the next vertex in the queue
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

graph.bfs(1)

