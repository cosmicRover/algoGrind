#BFS on a graph's nodes with inputs as [[nodes]]. Cycles are allowed. Nodes are ints

class BFSandDFS:
    #nodes -> [[source, destination]] in this exapmple we dont care 
    #about edge-weights. If edge-weight provided, we set the aside
    def findBFS(self, nodes:[[int]], start_node) -> [int]:
        #init ds to hold the graph and visited information
        graph = [set() for _ in range(len(nodes))]
        visited = [0] * len(nodes)
        bfs_order = []

        #create the graph
        for s, d in nodes:
            graph[s].add(d)

        #preparing queue, visited and append for start node
        queue = [start_node]
        visited[start_node] = 1
        bfs_order.append(start_node)

        #iterative approach to bfs using a queue.
        while queue:
            n = queue.pop(0)
            for node in graph[n]:
                #if a node is unvisited, we visit
                if visited[node] == 0:
                    bfs_order.append(node)
                    queue.append(node)
                    visited[node] = 1

        return bfs_order

    #dfs example
    def findDFS(self, nodes:[[int]], start_node) -> [int]:
        #init ds to hold the graph and visited information
        graph = [set() for _ in range(len(nodes))]
        visited = [0] * len(nodes)
        dfs_order = []

        #create the graph
        for s, d in nodes:
            graph[s].add(d)

        #preparing queue, visited and append for start node
        visited[start_node] = 1
        dfs_order.append(start_node)

        #Recursive approach to finding dfs order
        self.dfs(graph, visited, start_node, dfs_order)
        return dfs_order

    def dfs(self, graph, visited, node, order):
        for node in graph[node]:
            if visited[node] == 0:
                order.append(node)
                visited[node] = 1
                self.dfs(graph, visited, node, order)
         
input_arr = [[0,1], [0,2], [1,2], [2,0], [2,3], [3,3]]
input_arr_no_cycle= [[0,1], [0, 2], [2,4], [1,3], [3,5], [4,6], [4,7]]
bdfs = BFSandDFS()
print("BFS->>", bdfs.findBFS(input_arr, 2))
print("DFS->>", bdfs.findDFS(input_arr, 2))

