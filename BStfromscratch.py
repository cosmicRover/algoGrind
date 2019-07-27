class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

    def get(self):
        return self.value
    
    def set(self, value):
        self.value = value

class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, value):
        self.root = Node(value)
    
    def insert(self, value):
        if self.root is None:
            self.setRoot(value)
        else:
            self._insertANode(self.root, value)

    def getMin(self, value):
        return self._getTheMinNode(self.root, value)

    def _getTheMinNode(self, currentNode, value):
        if currentNode is None:
            return None

        while currentNode.left != None:
            currentNode = currentNode.left
        return currentNode

    def _insertANode(self, currentNode, value):

        if value <= currentNode.value:
            if currentNode.left:
                self._insertANode(currentNode.left, value)
            else:
                currentNode.left = Node(value)
        elif value > currentNode.value:
            if currentNode.right:
                self._insertANode(currentNode.right, value)
            else:
                currentNode.right = Node(value)

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node != None:
            self._printTree(node.left)
            print(str(node.value))
            self._printTree(node.right)

    def find(self, value):
        
        if self.root != None:
            return self._findANode(self.root, value)

    def _findANode(self, node, value):

        if node is None:
            return False
        elif value == node.value:
            return True
        elif value > node.value:
            return self._findANode(node.right, value)
        elif value <= node.value:
            return self._findANode(node.left, value)




bst = BST()
array = [4, 2, 77, 8, 12, 44]

for x in array:
    bst.insert(x)

bst.printTree()
print(bst.find(44))





        
