'''
Topological sort is when you pick a node and keep traveling till you hit the leaf node,
then you note down the leaf node. Topological order only works on a graph that has no cycle.
Therefore, only a DAG is compatible.

1) First step on any graph problem is to figure out a way to represent the input as a graph.
    In this example, the list of lists are being converted to graph adjacency list.
    graph is the adj-list of this example and since the courses are all ints we can 
    get away with a simple list of graph nodes

2) Create a DS to track node being visited, visited, and unvisited. Usually a dict
    or list with -1, 0, 1 to indicate the different states.

3) And finally, visit the nodes recursively. In this case, since we are prioritzing finding a leaf
    node, we utilize DFS

'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        #init DS to hold graph and visited states
        graph = [set() for _ in range(numCourses)]
        visited, orders = [0] * numCourses, []
        
        #create a graph. in this instance, destination comes before source
        for destination, source in prerequisites:
            graph[source].add(destination)
        
        #looop through the visited nodes using numCourses and visit all the nodes
        for node in range(numCourses):
            #if a node is unvisited and can visit it's neighbors, we keep going
            if visited[node] == 0 and self.dfs(graph, visited, node, orders):
                return 
        
        #since dfs will append the leaf node first, we reverse the array to get the top-order
        return orders[::-1]
            
    def dfs(self, graph, visited, node, orders):
        #mark node as being visited
        visited[node] = -1
        
        #visit the neighbors
        for x in graph[node]:
            if visited[x] == -1 or visited[x] == 0 and self.dfs(graph, visited, x, orders):
                return True
        
        #mark as visiting complete and append to order
        visited[node] = 1
        orders.append(node)
        return False