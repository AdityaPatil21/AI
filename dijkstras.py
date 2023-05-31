INF = float('inf')
V = 6

graph = [
    [0, 4, 6, INF, INF, INF],
    [4, 0, 6, 3, 4, INF],
    [6, 6, 0, 1, 8, INF],
    [INF, 3, 1, 0, 2, 3],
    [INF, 4, 8, 2, 0, 7],
    [INF, INF, INF, 3, 7, 0]
]

def dijkstra(graph, src):
    dist = [INF] * V  # Initialize distances to infinity
    dist[src] = 0  # Distance to the source vertex is 0

    visited = [False] * V  # Track visited vertices
    parent = [-1] * V  # Track parent vertices in the shortest path

    for _ in range(V):
        # Find the vertex with the minimum distance value
        u = min_vertex(dist, visited)
        visited[u] = True

        # Update distances of adjacent vertices
        for v in range(V):
            if not visited[v] and graph[u][v] != INF and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u  # Update the parent vertex

    # Print the shortest paths
    print("Source Vertex:", src)
    print("Vertex   Distance    Path")
    for v in range(V):
        print(f"{v:9}\t{dist[v]:9}\t", end="")
        if v != src:
            print_path(v, parent)
        print()

def min_vertex(dist, visited):
    min_dist = INF
    min_vertex = -1

    for v in range(V):
        if not visited[v] and dist[v] < min_dist:
            min_dist = dist[v]
            min_vertex = v

    return min_vertex

def print_path(v, parent):
    if parent[v] == -1:
        return
    print_path(parent[v], parent)
    print(f"-> {v}", end="")

dijkstra(graph, 0)


#Relaxation 
#if d(u) + C(u,v) < d(v)  0 + 20 =20, 20 < inf
#d(v)= d(u) + C(u,v) 
