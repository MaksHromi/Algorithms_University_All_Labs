class Graph:
    def __init__(self, vertices, directed=False, weighted=False):
        self.vertices = vertices
        self.directed = directed
        self.weighted = weighted
        self.adjacencyMatrix = self.initializeMatrix(vertices)
        self.adjacencyList = self.initializeList(vertices)

    def initializeMatrix(self, vertices):
        matrix = []
        for i in range(vertices):
            matrix.append([0] * vertices)
        return matrix

    def initializeList(self, vertices):
        lst = {}
        for i in range(vertices):
            lst[i] = []
        return lst

    def addEdge(self, source, destination, weight=1):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            self.adjacencyMatrix[source][destination] = weight
            self.adjacencyList[source].append({'node': destination, 'weight': weight})
            if not self.directed:
                self.adjacencyMatrix[destination][source] = weight
                self.adjacencyList[destination].append({'node': source, 'weight': weight})

    def printAdjacencyMatrix(self):
        print("Adjacency Matrix:")
        for row in self.adjacencyMatrix:
            print(row)

    def printAdjacencyList(self):
        print("Adjacency List:")
        for vertex in self.adjacencyList:
            print(f"{vertex}: {self.adjacencyList[vertex]}")

    def drawGraph(self):
        pass


def main():
    vertices = int(input("Podaj liczbę wierzchołków: "))
    graph = Graph(vertices)

    is_directed = input("Czy graf jest skierowany? (Tak/Nie): ").lower()
    if is_directed == "tak":
        graph.directed = True

    is_weighted = input("Czy graf jest ważony? (Tak/Nie): ").lower()
    if is_weighted == "tak":
        graph.weighted = True

    for i in range(graph.vertices):
        print(f"Wierzchołek {i}:")
        connections = input("Podaj połączenia (oddzielone przecinkami): ")
        edges = connections.split(",")
        for edge in edges:
            destination, weight = edge.split(":")
            if graph.weighted:
                graph.addEdge(i, int(destination), float(weight))
            else:
                graph.addEdge(i, int(destination))

        if i == graph.vertices - 1:
            graph.printAdjacencyMatrix()
            graph.printAdjacencyList()
            graph.drawGraph()


main()