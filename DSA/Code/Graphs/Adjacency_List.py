class Graph:
    def __init__(self, num_vertex):
        self.num_vertex = num_vertex
        self.graph = [[] for _ in range(num_vertex)]
        """ 
        - The __init__ function initializes the graph with the number of vertices.
        - It creates an adjacency list with the given number of vertices.
        - The adjacency list is represented as a list of lists of size num_vertex.
        - Each vertex has a list of adjacent vertices.
        - The graph is initialized with an empty list for each vertex.
        """
        
    # Add an edge between vertices u and v with weight
    def add_edge(self, u, v, directed = False, weight = 1):
        self.graph[u].append((v, weight))
        if not directed:
            self.graph[v].append((u, weight))
        """ 
        - Here, u refers to the starting vertex of the edge and v refers to the ending vertex of the edge.
        - The weight parameter specifies the weight of the edge between the two vertices.
        - The add_edge function adds an edge between two vertices in the graph.
        - It appends the vertex v and the weight of the edge to the adjacency list of vertex u.
        - If the graph is undirected, it appends the vertex u and the weight of the edge to the adjacency list of vertex v.
        """
    
    def print_adjacency_list(self):
        for i, row in enumerate(self.graph):
            print(i, end=" -> ")
            for edge in row:
                print( edge, end=" -> ")
            print()  # Move to the next line after each vertex

# Create a graph with 5 vertices
graph = Graph(5)

# Add edges to the graph
graph.add_edge(0, 1, directed = True, weight = 1)
graph.add_edge(0, 2, directed = True, weight = 1)
graph.add_edge(1, 2, directed = True, weight = 1)
graph.add_edge(1, 3, directed = True, weight = 1)
graph.add_edge(2, 3, directed = True, weight = 1)
graph.add_edge(3, 4, directed = True, weight = 1)

# Print the adjacency list of the graph
graph.print_adjacency_list()
