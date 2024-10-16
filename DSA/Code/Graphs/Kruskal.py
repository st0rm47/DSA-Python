def kruskal(graph):
    tree = {}
    for vertex in graph:
        tree[vertex] = vertex
    """ 
    - Each vertex starts as its own parent, creating disjoint sets.
    - This helps in tracking the connected components (subtrees) during the algorithm.
    """
    
    MST = []
    edges = []
    
    # Collect all edges from the graph.
    for start, neighbours in graph.items():
        for end, weight in neighbours.items():
            edges.append((weight, start, end))   
    edges.sort()  # Sort edges by weight (ascending order).
    """ 
    - Loop through the neighbors of each vertex and add edges to the list 'edges'.
    - Each edge is stored as (weight, start, end) to easily sort by weight.
    """
    
    # Implement Kruskal's algorithm to find the MST.
    for weight, start, end in edges:
        # Check if the start and end of the edge belong to different trees (subgraphs).
        if tree[start] != tree[end]:
            MST.append((start, end, weight))  # Add edge to the MST.
            
            # Update the tree dictionary to merge the sets containing 'start' and 'end'.
            old_tree = tree[end]
            new_tree = tree[start]
            for vertex, parent in tree.items():
                if parent == old_tree:
                    tree[vertex] = new_tree
    """
    - If the start and end vertices are not part of the same set (tree), they do not form a cycle.
    - Add the edge to the MST and then update 'tree' to merge the sets by updating all vertices 
      that belonged to the old set (tree[end]) to the new set (tree[start]).
    """
    
    return MST 

# Example graph
graph = {
    'A': {'B': 25, 'F': 5},
    'B': {'A': 25, 'C': 9, 'G': 6},
    'C': {'B': 9, 'D': 10},
    'D': {'C': 10, 'G': 11, 'E': 12},
    'E': {'D': 12, 'G': 16, 'F': 18},
    'F': {'E': 18, 'A': 5},
    'G': {'D': 11, 'E': 16, 'B': 6}
}

print(kruskal(graph))
