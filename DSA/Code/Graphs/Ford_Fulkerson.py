class Vertex:
    def __init__(self, name, source = False, sink = False):
        self.name = name
        self.source = source
        self.sink = sink
    """ 
    - name: name of the vertex
    - source: boolean value to check if the vertex is source
    - sink: boolean value to check if the vertex is sink
    """

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        
    """
    - start: starting vertex of the edge
    - end: ending vertex of the edge
    - capacity: capacity of the edge
    - flow: flow of the edge
    """

class FlowNetwork:
    def __init__(self):
        self.vertices = []
        self.network = {}
        
    """
    - vertices: list of vertices
    - network: dictionary to store the network
    """

    def get_source(self):
        for vertex in self.vertices:
            if vertex.source == True:
                return vertex
        return None
    """ 
    - returns the source vertex if it exists
    """
    
    def get_sink(self):
        for vertex in self.vertices:
            if vertex.sink == True:
                return vertex
        return None
    """
    - returns the sink vertex if it exists
    """
        
    def get_vertex (self, name):
        for vertex in self.vertices:
            if name == vertex.name:
                return vertex
        return None
    """
    - name: name of the vertex
    - returns the vertex with the given name
    """
    
    def vertex_in_network(self, name):
        for vertex in self.vertices:
            if vertex.name == name:
                return True
        return False
    
    """
    - name: name of the vertex
    - returns True if the vertex is in the network
    """
    
    def add_vertex(self, name, source = False, sink = False):
        if self.vertex_in_network(name):
            return None
        new_vertex = Vertex(name, source, sink)
        self.vertices.append(new_vertex)
        self.network[new_vertex.name] = []
        return new_vertex
    """
    - creates a new vertex and adds it to the network
    - returns the new vertex
    """
    def add_edges(self, start, end, capacity):
        if start == end:
            return None
        new_edge = Edge(start, end, capacity)
        self.get_vertex(start)
        self.get_vertex(end)
        self.network[start].append(new_edge)
        reverse_edge = Edge(end, start, 0)
        self.network[end].append(reverse_edge)
        return new_edge
    
    """
    - creates a new edge 
    - gets the start and end vertices of the edge
    - adds the edge to the network
    - creates a reverse edge with the end and start vertices of the edge
    - adds the reverse edge to the network
    - returns the new edge
    """
    
    def get_path(self, start, end, path):
        if start == end:
            return path
        for edge in self.network[start]:
            residual = edge.capacity - edge.flow
            if residual > 0 and not (edge, residual) in path:
                result = self.get_path(edge.end, end, path + [(edge, residual)])
                if result != None:
                    return result
                
    """
    - loops through the network to find a path from start to end
    - residual: the remaining capacity of the edge
    - if residual > 0 and the edge is not in the path, the function is called recursively,
    - WITH the end of the edge as the new start vertex and the path updated with the edge and the residual capacity of the edge
    - returns the path
    """
    
    def max_flow(self):
        source = self.get_source()
        sink = self.get_sink()
        if source == None or sink == None:
            return None
        path = self.get_path(source.name, sink.name, [])
        while path != None:
            flow = min(edge[1] for edge in path)
            for edge, _ in path:
                edge.flow += flow
                for reverse in self.network[edge.end]:
                    if reverse.end == edge.start:
                        reverse.flow -= flow
                        break
            path = self.get_path(source.name, sink.name, [])
        return sum(edge.flow for edge in self.network[source.name])
        
    
    """
    - gets the source and sink vertices
    - gets the path from source to sink
    - loops through the path and calculates the flow
    - updates the flow and residual capacity of the edge
    - gets the path from source to sink again
    - returns the sum of the flow
    """
    
fn = FlowNetwork()
fn.add_vertex('s', True, False)
fn.add_vertex('t', False, True)
for vertex_name in ['a', 'b', 'c', 'd']:
    fn.add_vertex(vertex_name)

fn.add_edges('s', 'a', 8)
fn.add_edges('a', 'b', 9)
fn.add_edges('d', 'b', 7)
fn.add_edges('s', 'd', 3)
fn.add_edges('c', 't', 5)
fn.add_edges('d', 'c', 4)
fn.add_edges('b', 't', 2)

max_flow = fn.max_flow()
print("Maximum Flow:", max_flow)