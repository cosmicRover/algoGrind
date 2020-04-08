import heapq
import collections
'''
Dijkstra solution
Time O(E + V log V) | Space O(E + V) for the graph
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, K: int) -> int:
	    
        #setup DS. The leftmost value is used for pq
        pq = [(0, src, K+1)]; #push starting values to pq + readjust k
        graph = collections.defaultdict(dict)
        
        #populate graph with flights. Use u, v as key index
        for u, v, w in flights:
            graph[u][v] = w
            
            
        print(graph)
        # key0: {key1: value1, key2: value2}
        #graph[key0] = {key1: value, key2: value}
        #graph[key1] = value1
        
        #traverse with pq
        while pq:
            cost, start, stops = heapq.heappop(pq)
            if start == dst: return cost
            
            if stops: #if stops > 1
                for dest in graph[start]:
                    heapq.heappush(pq, (cost+graph[start][dest], dest, stops-1)) #update cost, dest, K and push to pq
        
        else:
            return -1
