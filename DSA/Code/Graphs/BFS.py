class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = {node : False for node in graph}
        # Queue for BFS
        self.queue = []

    def bfs(self, node):
        # Traversal order
        traversal = []
        # Mark the node as visited and add it to the queue
        self.visited[node] = True
        # Add the node to the queue
        self.queue.append(node)
        # Continue until queue is empty
        while self.queue:
            # Pop the front element and mark it as visited
            current_node = self.queue.pop(0)
            traversal.append(current_node)
            # Add all neighbors to queue for traversal
            for neighbor in self.graph[current_node]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    self.queue.append(neighbor)
        print(traversal)
graph = {
  "A": ["B", "C"],
  "B": ["A", "D", "E"],
  "C": ["A", "F"],
  "D": ["B"],
  "E": ["B", "F"],
  "F": ["C", "E"]
}

bfs_instance = BFS(graph)
bfs_instance.bfs("A")
