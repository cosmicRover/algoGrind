class Vertex:

    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.visited = False

    def addNeighbor(self, vertex):

        neighborSet = set(self.neighbors)

        if vertex not in neighborSet:
            self.neighbors.append(vertex)
            self.neighbors.sort()


class adjListGraph:

    vertices = {}

    def addAVertex(self, vertex):

        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def addEdgeToVertex(self, vertexA, vertexB, isUndirected: bool):

        if vertexA in self.vertices and vertexB in self.vertices:
            self.vertices[vertexA].addNeighbor(vertexB)

            if isUndirected:
                self.vertices[vertexB].addNeighbor(vertexA)

    def printGraph(self):
        for key in sorted(list(self.vertices.keys())):
            print(str(self.vertices[key].name) +
                  " " + str(self.vertices[key].neighbors))

    def bfs(self, vertex):

        bfsPath = []
        queue = []
        result = self.bfsHelper(queue, vertex, bfsPath)
        print(result)

    def bfsHelper(self, queue, vertex, bfsPath):

        # setting the first passed in vertex to visited and appending it to path
        currentVertex = self.vertices[vertex.name]
        currentVertex.visited = True
        bfsPath.append(currentVertex.name)

        # add the neighbor nodes of first vertex
        for neighbor in currentVertex.neighbors:
            queue.append(neighbor)

        # using a queue we go level by level and pop the first element
        while len(queue) > 0:

            value = queue.pop(0)
            vertex = self.vertices[value[0]]

            # if the element wasnt visited, we visit it and set it visited flag
            if vertex.visited == False:
                vertex.visited = True
                bfsPath.append(vertex.name)

                # now we add it's neighbors for loop to continue
                for neighbor in vertex.neighbors:
                    queue.append(neighbor)

        return bfsPath


graph = adjListGraph()

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# adding the graph vertices
for vertex in vertices:
    graph.addAVertex(Vertex(vertex))

edges = ['AB', 'BC', 'CD', 'EF', 'DE', 'EA']
boolValues = [True, False, False, False, True, True]

# adding the edge pairs to the existing vertices
for edge, boolVal in zip(edges, boolValues):
    graph.addEdgeToVertex(edge[:1], edge[1:], boolVal)

graph.printGraph()
# graph.bfs(Vertex('C'))
graph.bfs(Vertex('A'))
# graph.bfs(Vertex('G'))
