def dijkstra(graph,start,end):
    
    #initialize the distance of all vertices to infinity 
    distance = {vertex : float ("infinity") for vertex in graph}
    
    #initialize the distance of the start vertex to 0
    distance[start] = 0
    
    #initialize the parent of all vertices to None
    parent = {vertex : None for vertex in graph}
    
    #store vertices with minimum distance from the start vertex
    queue = []
    
    #add the start vertex to the queue
    queue.append(start)
    
    while queue:
        curr_vertex = queue.pop(0)
        
        #for each neighbor of the current vertex
        for neighbor, weight in graph[curr_vertex].items():  
            if distance[neighbor] > distance[curr_vertex] + weight:
                distance[neighbor] = distance[curr_vertex] + weight
                parent[neighbor] = curr_vertex
                """ 
                - If the distance of a neighbor v from the start vertex is greater than the distance of current vertex + weight of the edge,
                - set the distance of v to the distance of current vertex + weight of the edge.
                - set the parent of v to the current vertex.
                """
                
                queue.append(neighbor)
                """
                - add the neighbor to the queue.
                - The above steps are repeated until the queue becomes empty.
                """
                
    path = []
    #construct the path from the start vertex to the end vertex
    while end:
        path.append(end)
        end = parent[end]
        """
        - The above steps are repeated until the end vertex becomes None.
        - The path from the start vertex to the end vertex is constructed by backtracking from the end vertex to the start vertex.
        """
    path.reverse()
    return distance[path[-1]], path
    
    
graph = {
    'A': {'B': 4, 'C': 4},
    'B': {'A': 4, 'C': 2},
    'C': {'A': 4, 'B': 2, 'D': 3, 'E': 1, 'F': 6},
    'D': {'C': 3, 'F': 2},
    'E': {'C': 1, 'F': 3},
    'F': {'C': 6, 'D': 2, 'E': 3},
}
distance, path = dijkstra(graph, 'A', 'F')
print("Shortest distance:", distance)
print("Path:", path)