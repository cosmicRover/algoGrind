#union find algo is useful when you need to find rot node of a collection of nodes
#union find with path compression. Path compression improves the root finding time to O(1)
#by directly linking to the parent

class UnionFind:

    #keep looking for i recursively
    def find(self, graph, i):
        if i != graph[i]:
            graph[i] = self.find(graph, graph[i])
        return graph[i]

    #insert one node as a value of the other
    def union(self, graph, i, j):
        pi, pj = self.find(graph, i), self.find(graph, j)
        if pi != pj:
            graph[pi] = pj

    #check if two nodes are connected
    def connected(self, graph, i, j):
        return self.find(graph, i) == self.find(graph, j)

    def run(self, connections, length):
        #init an empty graph
        graph = [i for i in range(length)]

        #union
        for i, j in connections:
            self.union(graph, i, j)

        #find
        for i in range(length):
            print("item ", i, ' -> component of ', self.find(graph, i))

        print(graph)


connections = [(0, 1), (1, 2), (0, 9), (5, 6), (6, 4), (5, 9), (3, 4), (7, 3), (8, 2)]
length = 10
uf = UnionFind()
uf.run(connections, length)