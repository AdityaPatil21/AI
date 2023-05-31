# Number of vertices in the graph
V = 6

# Number of edges in the graph
E = 10

# Parent array to track parent nodes
parent = [-1] * V

# Minimum spanning tree array
mst = []

# Edges in the graph
edges = [
    [0, 1, 1],
    [1, 3, 1],
    [2, 4, 1],
    [0, 2, 2],
    [2, 3, 2],
    [3, 4, 2],
    [1, 2, 3],
    [1, 4, 3],
    [4, 5, 3],
    [3, 5, 4]
]

# Printing MST
def print_mst():
    print("Minimum spanning tree formed is:\n")
    for edge in mst:
        print("From {0} --> To {1}  Weight -> {2}".format(edge[0], edge[1], edge[2]))

# Calculating total weight of MST
def calculate_mst_weight():
    total_weight = sum(edge[2] for edge in mst)
    print("Total weight of the minimum spanning tree (MST):", total_weight)

# Finding the absolute parent
def find(vertex):
    if parent[vertex] == -1:
        return vertex
    return find(parent[vertex])

# Making union of two disjoint sets
#This function performs the union of two disjoint sets by making one set's root the parent of the other set's root. It uses the find() function to find the absolute parents (roots) of the given vertices fromP and toP. It assigns the toP vertex as the parent of the fromP vertex by updating the parent array.

#Example:
#If parent = [-1, 0, 1, 1, 0], calling union(3, 4) would update parent to [-1, 0, 1, 1, 1], as it makes the root of the set containing vertex 3 (which is 1) the parent of the root of the set containing vertex 4 (which is also 1).
def union(fromP, toP):
    fromP = find(fromP)
    toP = find(toP)
    parent[fromP] = toP

# Get weight of an edge
def get_weight(edge):
    return edge[2]

# Finds MST using Kruskal's algorithm
def kruskals(edges, V, E):
    edges.sort(key=get_weight)  # Sort edges based on weight
    i = 0
    j = 0
    while i < V - 1 and j < E: #i represents the number of edges that have been added to mst & j -iterate over the sorted edges list
        fromP = find(edges[j][0])
        toP = find(edges[j][1])

        if fromP == toP:
            j = j + 1
            continue
        union(fromP, toP)
        mst.append(edges[j])
        i = i + 1

# Find MST using Kruskal's algorithm
kruskals(edges, V, E)

# Print the MST and its total weight
print_mst()
calculate_mst_weight()
#O(E log E + E log V).
#O(E + V).
