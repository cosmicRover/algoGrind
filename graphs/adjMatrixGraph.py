# graph with adjacency matrix supports both weighted and unweighted edges

# vertex class initiates with vertex name


class Vertex:
    def __init__(self, name):
        self.name = name


class AdjMatrixGraph:

    vertices = {}
    edges = []
    edgesIndices = {}

    def addAVertex(self, vertex):
        # as always check to see if the provided vertex is valid and it's not in the vertices dict
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            # add the vertex
            self.vertices[vertex.name] = vertex

            # add a row of 0's to the edges
            for row in self.edges:
                row.append('.')

            # and then add a column of 0's to the edges as well
            self.edges.append(['.'] * (len(self.edges) + 1))

            # finally, add the vertex to the edgeIndices dict
            self.edgesIndices[vertex.name] = len(self.edgesIndices)

            return True

        else:
            return False

    def addAnEdge(self, vertexA, vertexB, weight=1):
        if vertexA in self.vertices and vertexB in self.vertices:
            # adding the edge and their weights using the edgeIndices
            self.edges[self.edgesIndices[vertexA]
                       ][self.edgesIndices[vertexB]] = weight
            self.edges[self.edgesIndices[vertexB]
                       ][self.edgesIndices[vertexA]] = weight
            return True
        else:
            return False

    def printGraph(self):
        for v, i in sorted(self.edgesIndices.items()):
            print(v + ' ', end='')

            for j in range(len(self.edges)):
                print(self.edges[i][j], end='')
            print(' ')


graph = AdjMatrixGraph()

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# adding the graph vertices
for vertex in vertices:
    graph.addAVertex(Vertex(vertex))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH']
edgeWeights = [5, 7, 8, 1, 3, 9]

# adding the edge pairs to the existing vertices with weights
for edge, weights in zip(edges, edgeWeights):
    graph.addAnEdge(edge[:1], edge[1:], weights)

graph.printGraph()

"""
output
A .5..7.. 
B 5....8. 
C ......1 
D ....3.. 
E 7..3... 
F .8..... 
G ..1.... 
"""
