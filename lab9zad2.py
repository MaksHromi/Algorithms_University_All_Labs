def dfs(graph, current_node, visited=None):
    if visited is None:
        visited = set()

    print(current_node)
    visited.add(current_node)

    neighbors = graph[current_node]
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')