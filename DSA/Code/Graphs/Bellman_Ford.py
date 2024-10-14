def bellman(graph, source):

    #initialize distance and parent dictionaries
    distance = {vertex : float('inf') for vertex in graph}
    parent = {vertex : None for vertex in graph}
    
    #initialize the distance of the source vertex to 0
    distance[source] = 0
    
    #relax edges repeatedly
    for _ in range(len(graph)-1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distance[neighbor] > distance[vertex] + weight:
                    distance[neighbor] = distance[vertex] + weight
                    parent[neighbor] = vertex
                    
                    """ 
                    - If the distance of a neighbor v from the source vertex is greater than the distance of current vertex + weight of the edge,
                    - set the distance of v to the distance of current vertex + weight of the edge.
                    - set the parent of v to the current vertex.
                    """
    
    #detect negative cycle
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distance[neighbor] > distance[vertex] + weight:
                return None, None
            """ 
            - If the distance of a neighbor v from the source vertex is greater than the distance of current vertex + weight of the edge,
            - return None, None."""

    return distance, parent

graph = {
    'A': {'B': 4, 'C': 4},
    'B': {'A': 4, 'C': 2},
    'C': {'A': 4, 'B': 2, 'D': 3, 'E': 1, 'F': 6},
    'D': {'C': 3, 'F': 2},
    'E': {'C': 1, 'F': 3},
    'F': {'C': 6, 'D': 2, 'E': 3},
}

distance, parent = bellman(graph, 'A')
print ("Distance from source vertex to other vertices:", distance)
print ("Parent of each vertex:", parent)