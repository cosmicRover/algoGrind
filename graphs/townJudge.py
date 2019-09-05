# leetcode 997
# passes on regular test but not on submission

# transform the problem into a graph DS to see all the links


class Vertex:
    def __init__(self, name, visited=False):
        self.name = name
        self.neighbor = list()
        self.visited = False

    def addNeighbor(self, vertex):
        neighborSet = set(self.neighbor)

        if vertex not in neighborSet:
            self.neighbor.append(vertex)
            self.neighbor.sort()


class Solution(object):

    vertices = {}

    def addAVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def addEdgeToVertex(self, vertexA, vertexB):

        if vertexA in self.vertices and vertexB in self.vertices:
            self.vertices[vertexA].addNeighbor(vertexB)

    def printGraph(self):
        for key in sorted(list(self.vertices.keys())):
            print(str(self.vertices[key].name) +
                  " " + str(self.vertices[key].neighbor))

    def findJudge(self, N, trust):

        if trust == []:
            return 1 if N == 1 else -1*(1)

        potentialJudge = None

        for num1, num2 in trust:
            self.addAVertex(Vertex(num1))
            self.addAVertex(Vertex(num2))

        for num1, num2 in trust:
            self.addEdgeToVertex(num1, num2)

        for key in sorted(list(self.vertices.keys())):
            if self.vertices[key].neighbor == []:
                potentialJudge = self.vertices[key].name
                del self.vertices[potentialJudge]
                break

        for key in sorted(list(self.vertices.keys())):
            if potentialJudge not in self.vertices[key].neighbor:
                return -1

        self.printGraph()

        return potentialJudge
