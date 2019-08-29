# this relatively simple graph implementation is suitable graphs with unweighted edges. Better space efficiency

# vertex class to store the node vertices and their neighbors


class Vertex:

    # init with node name and it's neighbors
    def __init__(self, name):
        self.name = name
        self.neighborNodes = list()

    def addNeighbor(self, vertex):
        if vertex not in self.neighborNodes:
            self.neighborNodes.append(vertex)
            self.neighborNodes.sort()


class AdjGraph:

    # a dict of vertices with all of the vertex objects
    vertices = {}

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

                if key == vertexA:
                    value.addNeighbor(vertexB)
                if key == vertexB:
                    value.addNeighbor(vertexA)

    # printing out the sorted graph
    def printTheGraph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighborNodes))


graph = AdjGraph()

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# adding the graph vertices
for vertex in vertices:
    graph.addAVertex(Vertex(vertex))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH']

# adding the edge pairs to the existing vertices
for edge in edges:
    graph.addAnEdgeToAVertex(edge[:1], edge[1:])

graph.printTheGraph()
