# Set a large value to represent infinity
INF = float('inf')

# Number of vertices in the graph
V = 5

# Adjacency matrix representing the graph
G = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]

# Track the selected vertices (True if selected, False if not)
selected = [False] * V 

# Number of edges in the minimum spanning tree
no_edge = 0

# Select the first vertex (start from vertex 0)
selected[0] = True

# Print the edges and their weights
print("Edge : Weight\n")

# Total weight of the minimum spanning tree
mst_weight = 0

# Iterate until we select V-1 edges (minimum spanning tree)
while no_edge < V - 1:     #(the number of selected edges) is less than V-1 (the total number of vertices minus 1). This condition ensures that the loop terminates once the minimum spanning tree is constructed, consisting of V-1 edges.
    minimum = INF
    x = y = 0 #These variables will store the indices of the vertices that form the minimum weight edg
 
    # Find the minimum weight edge among the selected and unselected vertices
    for i in range(V):
        if selected[i]: # This condition checks if vertex i is already selected and part of the minimum spanning tree. If it is selected, the inner loop is executed to find the minimum weight edge.
            for j in range(V): #This loop iterates over all vertices (j) in the graph.
                if not selected[j] and G[i][j] and G[i][j] < minimum: #Within the nested loops, this condition checks if vertex j is not yet selected (not selected[j]), and there is an edge (G[i][j]) between vertices i and j with a weight smaller than the current minimum (G[i][j] < minimum). If these conditions are met, the minimum weight and the corresponding vertices (x and y) are updated.
                    minimum = G[i][j]
                    x = i
                    y = j
    
    # Print the edge and its weight
    print(x, "-", y, ":", G[x][y])

    # Mark the selected vertex as True
    selected[y] = True

    # Increment the edge count
    no_edge += 1

    # Add the weight of the selected edge to the total MST weight
    mst_weight += G[x][y]

# Print the total weight of the minimum spanning tree
print("\nTotal weight of the minimum spanning tree:", mst_weight)

#O(V^2) for adjaceny matric
#O((V + E) log V) for adjaceny list
# O(V) space
