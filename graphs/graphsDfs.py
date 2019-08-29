# this graph implementation is suitable graphs with unweighted edges and undirected paths. Better space efficiency
# vertex class to store the node vertices, their neighbors, discovey, finish time and the flags


class Vertex:

    # init with node name and it's neighbors
    def __init__(self, name):
        self.name = name
        self.neighborNodes = list()

        self.discovery = 0
        self.finish = 0
        self.visited = 'false'

    def addNeighbor(self, vertex):

        neighborSet = set(self.neighborNodes)

        if vertex not in neighborSet:
            self.neighborNodes.append(vertex)
            self.neighborNodes.sort()


class AdjGraph:

    # a dict of vertices with all of the vertex objects
    vertices = {}
    time = 0

    # to add a vertex, first check if the vertex you provided actually a valid vertex using "isinstance"
    # and then check if the vertex doesnt already exist in the vertices dictionary
    def addAVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    # To add an edge to a vertex, first check if the two vertexes exist in our list
    # if true, then iterate though the key, value of dict and when we hit the keys we are looking for
    # we add the neighbors as opposite to one another
    def addAnEdgeToAVertex(self, vertexA, vertexB):

        if vertexA in self.vertices and vertexB in self.vertices:

            for key, value in self.vertices.items():
                # if the graph was directed, we would only connect A with B and be done with it
                if key == vertexA:
                    value.addNeighbor(vertexB)
                if key == vertexB:
                    value.addNeighbor(vertexA)
            return True
        else:
            return False

    # printing out the sorted graph
    def printTheGraph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighborNodes) + " discovery: " +
                  str(self.vertices[key].discovery) + " finish: " + str(self.vertices[key].finish) + " flag: " + str(self.vertices[key].visited))

    def _dfs(self, vertex, dfsStack):
        currentVertex = self.vertices[vertex.name]

        currentVertex.visited = 'true'
        currentVertex.discovery = self.time
        self.time += 1
        dfsStack.append(currentVertex.name)

        for v in currentVertex.neighborNodes:
            if self.vertices[v].visited == 'false':
                self._dfs(self.vertices[v], dfsStack)

        currentVertex.visited = 'dead-end'
        currentVertex.finish = self.time
        self.time += 1
        return dfsStack

    def dfsRecursive(self, vertex):
        dfsStack = []
        self.time = 1
        result = self._dfs(vertex, dfsStack)
        print("dfs path -> ", result)


graph = AdjGraph()

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# adding the graph vertices
for vertex in vertices:
    graph.addAVertex(Vertex(vertex))

edges = ['AB', 'BC', 'CD', 'EF', 'GA', 'BG', 'DE']

# adding the edge pairs to the existing vertices
for edge in edges:
    graph.addAnEdgeToAVertex(edge[:1], edge[1:])

# performing dfs on every node
# for vertex in vertices:
graph.dfsRecursive(Vertex('G'))

graph.printTheGraph()
