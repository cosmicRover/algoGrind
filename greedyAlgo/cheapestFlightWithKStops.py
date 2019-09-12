from collections import defaultdict
import heapq

from collections import defaultdict
import heapq

class Solution:

    def findCheapestPrice(self, n, flights, src, dst, k):

        #init adjDict to hold the parent - child vertex with weight
        adjDict = collections.defaultdict(dict)

        #populate the adjDict from the flights, with start, end as keys
        for parent, child, weight in flights:
            adjDict[parent][child] = weight

        #init the priority queue heap with 3 vals. cost, child(src), k+1 stop. we add one so we can loop at least once
        pq = [(0, src, k+1)]
        seen = set()  # keep track of the visited nodes so we dont visit duplicates

        while pq:
            #pop from heap
            cost, child, K = heapq.heappop(pq)

            #add it to the set
            seen.add(child)

            #if we get to the destination, return cost
            if child == dst:
                return cost

            #we push to heap fir the popped path k is > 0
            if K > 0:
                # loop through the values for the key
                for value in adjDict[child]:

                    # if it isn't visited, update the cost with the cost from adjDic and  push to pq
                    if value not in seen:
                        heapq.heappush(
                            pq, (cost + adjDict[child][value], value, K-1))

        return -1
