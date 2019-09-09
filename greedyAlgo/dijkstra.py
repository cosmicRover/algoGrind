graph = {'a':{'b':10, 'c':3}, 'b':{'c':1, 'd':2}, 'c':{'b':4, 'd':8, 'e':2}, 'd':{'e':7}, 'e':{'d':9}}

def dijkstra(graph, startVertex, destinationVertex):
    
    # init vals
    shortestDistance = {}
    previous = {}
    unseenNodes = graph
    infinity = float("inf")
    path = []

    #set the shortest path dict to infinity
    for node in unseenNodes:
        shortestDistance[node] = infinity
    
    #set the start point to 0
    shortestDistance['a'] = 0

    print("initial -> ", shortestDistance)

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortestDistance[node] < shortestDistance[minNode]:
                minNode = node

        
        for childNode, weight, in graph[minNode].items():
            if weight + shortestDistance[minNode] < shortestDistance[childNode]:
                shortestDistance[childNode] = weight + shortestDistance[minNode]
                previous[childNode] = minNode
        unseenNodes.pop(minNode)

    print(shortestDistance)

    currentNode = destinationVertex
    while currentNode != startVertex:
        path.insert(0, currentNode)
        currentNode = previous[currentNode]
    path.insert(0, startVertex)
    
    print("shortest distance to destination is -> ", shortestDistance[destinationVertex])
    print(path)



dijkstra(graph, 'a', 'd')
