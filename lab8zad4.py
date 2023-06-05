class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((item, priority))

    def dequeue(self):
        min_priority = float('inf')
        min_item = None
        min_index = None
        for i, (item, priority) in enumerate(self.queue):
            if priority < min_priority:
                min_priority = priority
                min_item = item
                min_index = i
        if min_index is not None:
            del self.queue[min_index]
        return min_item

    def isEmpty(self):
        return len(self.queue) == 0


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacencyList = {}

    def addEdge(self, source, destination, weight):
        if source not in self.adjacencyList:
            self.adjacencyList[source] = []
        self.adjacencyList[source].append({'node': destination, 'weight': weight})

    def dijkstra(self, startNode):
        distances = {}
        visited = {}
        previous = {}
        pq = PriorityQueue()

        for vertex in self.adjacencyList:
            if vertex == startNode:
                distances[vertex] = 0
                pq.enqueue(vertex, 0)
            else:
                distances[vertex] = float('inf')
                pq.enqueue(vertex, float('inf'))
            previous[vertex] = None

        while not pq.isEmpty():
            current = pq.dequeue()
            visited[current] = True

            if current in self.adjacencyList:
                for neighbor in self.adjacencyList[current]:
                    neighbor_node = neighbor['node']
                    neighbor_weight = neighbor['weight']
                    if neighbor_node not in visited:
                        distance = distances[current] + neighbor_weight
                        if distance < distances[neighbor_node]:
                            distances[neighbor_node] = distance
                            previous[neighbor_node] = current
                            pq.enqueue(neighbor_node, distance)

        return distances, previous

    def getShortestPath(self, previous, destination):
        path = []
        current = destination
        while current is not None:
            path.insert(0, current)
            current = previous[current]
        return path


def main():
    graph = Graph(6)

    graph.addEdge("A", "B", 2)
    graph.addEdge("A", "C", 4)
    graph.addEdge("B", "C", 1)
    graph.addEdge("B", "D", 7)
    graph.addEdge("C", "E", 3)
    graph.addEdge("D", "E", 2)
    graph.addEdge("D", "F", 5)
    graph.addEdge("E", "F", 1)

    startNode = "A"
    distances, previous = graph.dijkstra(startNode)

    for vertex in distances:
        print(f"Najkrótsza droga z wierzchołka {startNode} do {vertex}: {distances[vertex]}")
        path = graph.getShortestPath(previous, vertex)
        print(f"Ścieżka: {' -> '.join(path)}")
        print("---------------------------")


main()