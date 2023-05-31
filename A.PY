from queue import PriorityQueue

def aStarAlgo(start_node, stop_node):
    open_set = PriorityQueue()  # Priority queue to store nodes to be explored
    open_set.put((0, start_node))  # Add the start node to the priority queue with priority 0
    g = {start_node: 0}  # Dictionary to store the distance from the start node to each node
    parents = {start_node: None}  # Dictionary to store the parent node for each node in the path

    while not open_set.empty():
        current_node = open_set.get()[1]  # Get the node with the lowest priority (f(n) value)
#If no node is selected (i.e., n is None), it means that a path from the start node to the goal node does not exist, and the algorithm terminates.
        if current_node == stop_node: #n is equal to the goal node
            # Path found, reconstruct the path from the goal node to the start node
            path = [] # to store the nodes in the reconstructed path.
            cost = g[current_node]#set cost (accumulated weight) of reaching the current_node to cost var
            while current_node is not None:
                path.append(current_node)#Append the current_node to the path list.
                current_node = parents[current_node]#Update the current_node to its parent node by accessing parents[current_node]
            path.reverse() #Reverse the path list to obtain the correct order from start to goal.
            return path, cost

        for neighbor, weight in get_neighbors(current_node):#If a neighbor node is already in the open_list or closed_list, the algorithm checks if updating its g value with the current node n results in a shorter path. If it does, the g value and parent node are updated.
            new_g = g[current_node] + weight
            if neighbor not in g or new_g < g[neighbor]:#If a neighbor node is not in the open_list or closed_list, it means that it has not been visited yet. The algorithm adds it to the open_list, updates its parent node, and calculates its g value
                # Update g(n) value and priority if a shorter path is found
                g[neighbor] = new_g
                priority = new_g + heuristic(neighbor)
                open_set.put((priority, neighbor))
                parents[neighbor] = current_node

    return None, None

def get_neighbors(node):
    # Return the neighbors of the given node from the graph
    return Graph_nodes.get(node, [])

def heuristic(node):
    # Heuristic function to estimate the cost from the current node to the goal node
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist.get(node, float('inf'))

# Define your graph here
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

# Example usage:
path, cost = aStarAlgo('A', 'G')
if path:
    print("Path found:", path)
    print("Cost:", cost)
else:
    print("Path does not exist!")
#Iteration 1:

'''The node 'A' is selected as it is the only node in the open_list.

Since 'A' is not the goal node, the algorithm proceeds to explore its neighbors.

The get_neighbors function is called for node 'A', which returns [('B', 2), ('E', 3)].

The neighbor 'B' is selected with a weight of 2.

'B' is not in the open_list or closed_list, so it is added to the open_list. Its parent is set to 'A', and its g value is calculated as 0 + 2 = 2.

The neighbor 'E' is selected with a weight of 3.

'E' is not in the open_list or closed_list, so it is added to the open_list. Its parent is set to 'A', and its g value is calculated as 0 + 3 = 3.

The open_list now contains ['B', 'E'].

The next node to be selected from the open_list is 'B' since it has the lowest f = g + h value.
open_list: ['A']
closed_list: []
g values: {'A': 0}
parent: {'A': 'A'} Considering parent is itself
Iteration 2:

open_list: ['B', 'E']
closed_list: ['A']
g values: {'A': 0, 'B': 2, 'E': 3}
parent: {'A': 'A', 'B': 'A', 'E': 'A'}'''
