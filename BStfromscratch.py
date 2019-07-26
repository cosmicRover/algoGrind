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

    def find(self, value):
        return self._findANode(value)

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

    # problem finding anything else but the root
    def _findANode(self, value):

        currentNode = self.root

        while currentNode != None:

            if currentNode.value == value:
                return True
            elif currentNode.value <= value:
                currentNode = currentNode.left
            elif currentNode.value > value:
                currentNode = currentNode.right

        return False


bst = BST()
array = [4, 2, 77, 8, 12, 44]

bst.insert(5)
bst.insert(2)
bst.insert(19)
bst.printTree()
print(bst.find(19))





        