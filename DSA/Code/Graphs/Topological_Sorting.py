def topological_sorting(graph):
    sorted_vertices = []
        
    #calculate in-degrees of all vertices
    in_degrees = {v: 0 for v in graph}
    
    #calculate in-degrees of all vertices
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1
            """ 
            - for each vertex v in the adjacency list of u, 
            - increment the in-degree of v by 1.
            """
    
    #store vertices with in-degree 0
    queue = []
    for v in in_degrees:
        if in_degrees[v] == 0:
            queue.append(v)
            """ 
            - for each vertex v in the graph,
            - if the in-degree of v is 0, add v to the queue.
            """
    
    while queue:
        u = queue.pop(0)
        sorted_vertices.append(u)
        """ 
        - pop a vertex u from the queue.
        - add u to the sorted list.
        """
    
        #decrement in-degrees of all neighbors of u
        for v in graph[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                queue.append(v)
                """ 
                - All the neighbors of u have their in-degrees decremented by 1.
                - If the in-degree of a neighbor v becomes 0, add v to the queue.
                - The above steps are repeated until the queue becomes empty.
                """
                
    if len(sorted_vertices) == len(graph):
        return sorted_vertices
    
graph = { 
    'B': ['E', 'C'],
    'A': ['C', 'D'],
    'C': ['D'],
    'D': [],
    'E': ['A', 'C']
}
print(topological_sorting(graph))