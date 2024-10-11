class Graph:
    def __init__(self, num_vertex):
        self.num_vertex = num_vertex
        self.graph = [[0 for _ in range(num_vertex)] for _ in range(num_vertex)]
        """ 
        - The __init__ function initializes the graph with the number of vertices.
        - It creates an adjacency matrix with the given number of vertices.
        - The adjacency matrix is represented as a 2D list of size num_vertex x num_vertex.
        - The graph is initialized with all edge weights set to 0.        
        """

    # Add an edge between vertices u and v with weight
    def add_edge(self, u, v, directed = False, weight = 1):
        self.graph[u][v] = weight       
        if not directed:
            self.graph[v][u] = weight
                
        """ 
        - Here, u refers to the starting vertex of the edge and v refers to the ending vertex of the edge.
        - The weight parameter specifies the weight of the edge between the two vertices.
        - The add_edge function adds an edge between two vertices in the graph.
        - It sets the weight of the edge between the two vertices in the adjacency matrix.
        - If the graph is undirected, it sets the weight of the edge between v and u as well.
        """
    
    def print_adjacency_matrix(self):
        for row in self.graph:
            print(row)
    
# Create a graph with 5 vertices
graph = Graph(5)

# Add edges to the graph
graph.add_edge(0, 1, weight = 1)
graph.add_edge(0, 2, weight = 1)
graph.add_edge(1, 2, weight = 1)
graph.add_edge(1, 3, weight = 1)
graph.add_edge(2, 3, weight = 1)
graph.add_edge(3, 4, weight = 1)

# Print the adjacency matrix
graph.print_adjacency_matrix()



