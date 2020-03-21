'''
Krushkal's algorithm uitlizes the Union find data srtucture to find the minimum cost to visit all nodes
using the edge-weights that are associated with the vertices.
'''

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])

    #search for root
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    #unions two vertices x, y by rank
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        #assign a smaller rank
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []

        unSortIdx = 0; sortIdx = 0

        #sort items using edge weighths
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [] 
        rank = []

        #init parent and rank with starter values
        for node in range(self.v):
            parent.append(node)
            rank.append(0)

        while unSortIdx < self.v:

            #unpack the items, pick cheapest edge weight and inc index for iteration
            u, v, w = self.graph[unSortIdx]
            unSortIdx += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            #if an edge dont cause cycle, include in result and inc index
            if x != y:
                sortIdx += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("Following are the edges in the constructed MST")
        for u, v, w in result:
            print (u,v,w)


g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4)

g.kruskal()
                

    