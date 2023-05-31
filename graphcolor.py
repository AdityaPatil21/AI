# helper function to check color assignment is safe or not
def isSafe(node, color, graph, N, col):
    # check each neighbor of node for color col
    for k in range(N):
        # neighbor is not the current node
        # ensures we consider only the neighbors of the current node and not the node itself
        #color[k] == col: Checks if the neighbor vertex k has the same color (col) as the one we are considering for the current vertex node.
        if k != node and graph[k][node] == 1 and color[k] == col:
            return False
    return True

# recursive function
def solve(node, color, graph, M, N):
    # if node is the last node, the graph is colored
    if node == N:
        return True
    
    # check for each color if it can be assigned to the node or not
    for col in range(1, M+1): #col=1 ie color 1
        # check if color is safe or not
        if isSafe(node, color, graph, N, col):
            color[node] = col  # assign color to node
            # check for the next node
            if solve(node+1, color, graph, M, N):
                return True
            # color[node] = 0: This line backtracks by resetting the color assigned to the current vertex node to 0, indicating that it has no color assigned. This is necessary to explore different color assignments for the current vertex and continue the search for a valid coloring.
            color[node] = 0

# driver function
def GraphColoring(graph, M, N):
    # stores color assigned to each node
    color = [0] * N
    # call the recursive function to check if the graph can be colored or not
    if solve(0, color, graph, M, N):
        return True
    return False

# Example usage
Graph = [[0, 1, 1, 0, 0],
         [1, 0, 0, 1, 0],
         [1, 0, 0, 1, 1],
         [0, 1, 1, 0, 1],
         [0, 0, 1, 1, 0]]
N = 5  # number of vertices
M = 3  # number of colors

# call the GraphColoring function with the given graph, number of colors, and number of vertices
print(GraphColoring(Graph, M, N))




"""

what is graph colouring problem

ChatGPT
The graph coloring problem is a classic problem in graph theory and computer science. It involves assigning colors to the vertices of a graph in such a way that no two adjacent vertices share the same color. The goal is to find the minimum number of colors required to color the graph.

Formally, given an undirected graph G = (V, E), where V represents the set of vertices and E represents the set of edges, the graph coloring problem asks whether it is possible to assign colors to the vertices such that no two adjacent vertices have the same color.

The graph coloring problem has various real-world applications, including scheduling problems, register allocation in compilers, timetabling, frequency assignment in wireless communication, and map coloring.

The problem is often formulated as an optimization problem, where the objective is to minimize the number of colors used. This is known as the minimum vertex coloring problem. Finding the minimum number of colors required to color a graph is an NP-hard problem, which means that no known efficient algorithm exists to solve it for all instances.

There are different algorithms and heuristics to tackle the graph coloring problem, including backtracking algorithms like the Welsh-Powell algorithm and the DSatur algorithm, as well as other approaches like greedy coloring, genetic algorithms, and constraint programming.

Graph coloring problems can be categorized based on additional constraints or variations, such as edge coloring (assigning colors to edges instead of vertices), vertex coloring with additional constraints (e.g., avoiding adjacent vertices of the same color with a specific distance), and more.

Overall, the graph coloring problem is a fascinating and challenging problem in graph theory with applications in various domains.





User
how to solve graph colouring problem using back tracking ?

ChatGPT
To solve the graph coloring problem using backtracking, you can follow these general steps:

Represent the graph: Start by representing the given graph as an adjacency matrix or an adjacency list. The graph should be represented in a way that you can easily access the neighbors of each vertex.

Initialize data structures: Initialize a list or array to store the color assignments for each vertex. Initially, all vertices can be assigned a special value (e.g., 0) to indicate that they are not yet assigned a color.

Implement the backtracking algorithm:

Choose a vertex: Start by choosing a vertex from the graph.
Assign a color: Assign a color to the chosen vertex. Choose a color that is not already used by its adjacent vertices.
Check validity: After assigning a color, check if it is a valid assignment. This means that none of the adjacent vertices share the same color.
Backtrack: If the current assignment is not valid, undo the assignment and try a different color. Backtrack to the previous vertex and repeat the process.
Repeat: Continue this process for all remaining vertices in the graph until a valid solution is found or all possibilities are exhausted.
Optimize the algorithm (optional): You can add heuristics or additional constraints to improve the efficiency of the backtracking algorithm. For example, you can choose the vertices in a specific order (e.g., based on degree) or use a technique called "forward checking" to prune branches early if they are not valid.

Output the solution: Once a valid coloring is found (i.e., all vertices are assigned unique colors), output the color assignments for each vertex.

It's important to note that the graph coloring problem is an NP-hard problem, so finding an optimal solution for large graphs may be computationally expensive. Therefore, the backtracking algorithm may not be practical for very large graphs. However, it can be used effectively for smaller graphs or instances with specific constraints.

Implementing a backtracking algorithm for graph coloring requires a good understanding of graph theory, data structures, and recursion. It involves careful management of states, constraints, and backtracking steps.
"""
