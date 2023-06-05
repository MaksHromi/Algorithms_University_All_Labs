from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque()

    visited.add(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()
        print(current_node)

        neighbors = graph[current_node]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')