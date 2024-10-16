def prim(graph, start):
    
    tree = {}  # Dictionary to store the MST
    for vertex in graph:
        tree[vertex] = None
    tree[start] = start  # Start vertex has no parent
    """ 
    - Initialize the tree dictionary with all vertices as keys and None as values.
    - The value of the start vertex is set to itself to indicate it has no parent.
    """
    
    MST = []  # List to store the MST edges
    
    while None in tree.values():
        min_weight = float('inf')
        min_edge = None
        
        for vertex in tree:
            if tree[vertex] is not None:
                for neighbour, weight in graph[vertex].items():
                    if tree[neighbour] is None and weight < min_weight:
                        min_weight = weight
                        min_edge = (vertex, neighbour, weight)
        """ 
        - Find the minimum weight edge that connects a vertex in the MST to a vertex outside the MST.
        - The edge is stored as (start, end, weight) to be added to the MST.
        """
        
        if min_edge:
            start, end, weight = min_edge
            tree[end] = start
            MST.append((start, end, weight))
        """
        - Update the tree dictionary to include the new edge in the MST.
        - The 'end' vertex of the edge is added to the MST with 'start' as its parent.
        """
        
        
    return MST

graph = {
    'A': {'B': 25, 'F': 5},
    'B': {'A': 25, 'C': 9, 'G': 6},
    'C': {'B': 9, 'D': 10},
    'D': {'C': 10, 'G': 11, 'E': 12},
    'E': {'D': 12, 'G': 16, 'F': 18},
    'F': {'E': 18, 'A': 5},
    'G': {'D': 11, 'E': 16, 'B': 6}
}

mst = prim(graph, 'A')
for (start, end, weight) in mst:
    print(f"{start} - {end} : {weight} ")