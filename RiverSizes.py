# Problem M 14
# Solution
# Time O(w*h) | Space O(w*h) where w is width of the matrix and h is the height

def riverSize(matrix):
    sizes = [] # will contain the sizes of the rivers
    
    # a bool representation of the original matrix where it is being init as False 
    # for every single values. Set it to true when we visit a particular element
    visited =[[False for value in row] for row in matrix]
    
    # iterating through the 2d array
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # if column i and row j is visited, we continue with the next iteration of the loop
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

# visits the node and checks for a 0 or 1
def traverseNode(i, j, matrix, visited, sizes):
    
    # init currentNode and the target nodes to explore
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    
    # while nodesToExplore has a length
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop() # pop the node
        
        # set the row and column
        i = currentNode[0]
        j = currentNode[1]
        
        # if already visited, continue with the next iteration
        if visited[i][j]:
            continue
        
        # since we are visiting it now, we set the value of 2d array to true
        visited[i][j] = True

        # also if it's not a 1 i.e. 0, we proceed to nect iteration
        if matrix[i][j] == 0:
            continue

        # inc riverSize when we encounter 1
        currentRiverSize += 1

        # gets the unvisited neighbors of the current node
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)

        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)

    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []

    # checks all four sides of the matrix and appends ro the array to return
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])
    return unvisitedNeighbors