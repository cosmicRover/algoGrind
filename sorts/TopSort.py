# Given a DAG, what is the topologically sorted output of it?

from collections import defaultdict

def topSort(graph:[[str]]):
    
    # init the adjList if the input isn't in a adjList format
    # visited just keeps track of visited nodes
    adjList = defaultdict(list)
    visited = defaultdict(dict)

    #transform input into adjList
    for x, y in graph:
        adjList[x].append(y)
        visited[x] = False
    
    # the final top sorted output
    output = []

    # for each node in visited, call sort reccursively
    for node in list(visited):
        sort(node, visited, adjList, output)
    
    print(output)
    print(visited)


# calls itself reccursively for each unvisited nodes
def sort(vertex, visited, adjList, output):
    if not visited[vertex]:
        visited[vertex] = True

        for neighbor in adjList[vertex]:
            sort(neighbor, visited, adjList, output)
        output.insert(0, vertex)




g = [['A', 'B'], ['B', 'C'], ['B', 'F'], ['C', 'D'], ['D', 'E'], ['K', 'A'] ]
topSort(g)