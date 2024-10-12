class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = {node : False for node in graph}
        
    def dfs(self, graph, node):
        # Traversal order
        traversal = []
        # Stack for DFS
        stack = [node]
        #Continue until stack is empty
        while stack:
            # Pop the top element and mark it as visited
            current_node = stack.pop()
            # If not visited, add in visited list and traversal list
            if not self.visited[current_node]:
                self.visited[current_node] = True
                traversal.append(current_node)
                # Add all neighbors to stack for traversal
                for neighbor in self.graph[current_node]:
                    stack.append(neighbor)
                    
        return traversal
        
graph = {
  "A": ["B", "C"],
  "B": ["A", "D", "E"],
  "C": ["A", "F"],
  "D": ["B"],
  "E": ["B", "F"],
  "F": ["C", "E"]
}

dfs_instance = DFS(graph)
print(dfs_instance.dfs(graph,"A"))

        