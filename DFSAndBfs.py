# Problem E 3 and M 13
# Solutions


# the Node class
class Node:

    # init the children and the nodes
    def __init__(self, node):
        self.children = []
        self.node = node

    # add a node to the children array
    def addChild(self, node):
        self.children.append(Node(node))

    # Time O(v+e) where v is the nodes and e is the branches connected to the nodes
    # Space O(v) 
    # append a node to the array first and then iterate through 
    # the children while calling dfs recursively. Return the array in the end
    def depthFirstSearch(self, array):
        array.append(self.node)
        for child in self. children:
            child.depthFirstSearch(array)
        return array

    # Time O(v+e) just like dfs and Space O(v)
    # init a queue (simple array) to keep track of the children and keep popping the first one
    # to visit it's children. Do it till the queue is empty
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            currentNode = queue.pop(0)
            array.append(currentNode.node)
            for child in currentNode.children:
                queue.append(child)
        return array