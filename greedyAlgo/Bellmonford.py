class BellmanFord:

    def findShoretestEdges(self, edgeList, numberOfVertices, startVertex):

        # init the distance list with inf and a length of #of vertices.
        # Then set the starting point distance to 0
        distance = [float("inf") for _ in range(numberOfVertices)]
        distance[0] = 0

        # condition logic that dictates if we are unable to relax an edge further
        # thus signaling that we had reached the optimal solution early
        relaxedAnEdge: bool = True

        # for each vertex, apply the relaxation
        for _ in range(numberOfVertices - 1):
            if relaxedAnEdge:
                relaxedAnEdge = False
                for parent, child, cost in edgeList:
                    # relaxation
                    if distance[parent] + cost < distance[child]:
                        distance[child] = distance[parent] + cost
                        relaxedAnEdge = True

        # run the algo one more time to detect nodes that are part of negative cycles
        # a negative cycle occours if we can find better solutions beyond the optimal solution
        relaxedAnEdge = True

        for _ in range(numberOfVertices - 1):
            if relaxedAnEdge:
                relaxedAnEdge = False
                for parent, child, cost in edgeList:
                    if distance[parent] + cost < distance[child]:
                        distance[child] = float("-inf")
                        relaxedAnEdge = True

        print(distance)


bf = BellmanFord()

inputList = [[0, 1, 1], [1, 2, 1], [2, 4, 1], [4, 3, -3],
             [3, 2, 1], [1, 5, 4], [1, 6, 4], [5, 6, 5], [6, 7, 4], [5, 7, 3]]
bf.findShoretestEdges(inputList, 9, 0)