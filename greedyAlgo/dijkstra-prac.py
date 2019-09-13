# Practicing me some of the all powerful Dijkstra
# find the cheapest path to one node to it's destination node

# import some collections + prirority queue heapq modules for less boiler plate
from collections import defaultdict
import heapq


class Dijkstra:

    def findCheapestPath(self, numberOfNodes, paths, startPoint, destination):

        # init the adjDict to hold parent, child and their weights
        adjDict = defaultdict(dict)

        # populate the adjDict from the input
        for parent, child, weight in paths:
            adjDict[parent][child] = weight

        # setup a priority queue with cost-to-vertex
        # init with cost of 0 for the startingPoint
        pq = [(0, startPoint)]

        # init a set to keep track of the vertices that we visited
        # a set will prevent having duplicate copies

        visisted = set()

        # loop through the priority queue and pop them
        while pq:

            # pop the vertex with lowest cost from the priority queue
            cost, vertex = heapq.heappop(pq)

            # add to the visisted set
            visisted.add(vertex)

            # if the popped vertex is the same as destination, return cost cause we had reached out destination
            if vertex == destination:
                return cost

            # if vertex isn't destination, loop through the adjDict and add the unvisited vertices to the pq
            if vertex != destination:

                for value in adjDict[vertex]:
                    if value not in visisted:
                        # while adding to pq, make sure to update the accumulated cost of reaching the vertex
                        heapq.heappush(
                            pq, (cost + adjDict[vertex][value], value))

        return -1  # if none exist


graph = Dijkstra()
paths = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
length = 3
destination = 2
start = 0

print(graph.findCheapestPath(length, paths, start, destination))
