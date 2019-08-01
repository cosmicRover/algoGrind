class Node(object):
    def __init__(self, data):
        self.data = data
        self.previousNode= None
        self.nextNode = None


class DoublyLinkedList(object):
    def __init__(self):
        self.headNode = None
        self.tailNode = None

    # Time O(1) | O(1) Space
    def setHead(self, nodeToInsert):
        if self.headNode is None:
            newNode = Node(nodeToInsert)
            self.headNode = newNode
            self.tailNode = newNode

    # Time O(1) | O(1) Space
    def insertBeofreHeadNode(self, nodeToInsert):
        if self.headNode is None:
            self.setHead(nodeToInsert)
            return
        else:
            newNode = Node(nodeToInsert)
            tempNode = self.headNode
            self.headNode = newNode
            self.headNode.nextNode = tempNode
            tempNode.previousNode = newNode

    # Time O(1) | O(1) Space
    def insertAfterTailNode(self, nodeToInsert):
        if self.headNode is None:
            self.setHead(nodeToInsert)
            return
        else:
            newNode = Node(nodeToInsert)
            self.tailNode.nextNode = newNode
            newNode.previousNode = self.tailNode
            self.tailNode = newNode

    # Time O(p) where p is the distance to the position | O(1) Space
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.insertBeofreHeadNode(nodeToInsert)
            return
        
        currentNode = self.headNode
        positionCounter = 1
        
        while currentNode is not None and positionCounter != position:
            currentNode = currentNode.nextNode
            positionCounter += 1

        return self.insertBeforeANode(currentNode, nodeToInsert)
        
    def insertBeforeANode(self, node, nodeToInsert):
        newNode = Node(nodeToInsert)
        tempNode = node

        node.previousNode.nextNode = newNode
        newNode.nextNode = tempNode
        tempNode.previousNode = newNode
        return
    
    # Time O(N) | O(1) Space
    def searchForAValue(self, value):
        if self.headNode is None:
            return False
        currentNode = self.headNode

        while currentNode:
            currentNode = currentNode.nextNode
            if currentNode.data == value:
                return True
        return False

    # Time O(N) | O(N) Space because of the array we are creating 
    def printTheList(self):
        children = []
        currentNode = self.headNode

        while currentNode:
            children.append(currentNode.data)
            currentNode = currentNode.nextNode
        return children

    # Time O(1) | O(1) Space
    def peekHead(self):
        return self.headNode.data

    # Time O(1) | O(1) Space
    def peekTail(self):
        return self.tailNode.data



DLL = DoublyLinkedList()
array = [2, 4, 7, 8, 9, 10]
for x in array:
    DLL.insertBeofreHeadNode(x)

array2 = [34, 54, 66, 88]
for x in array2:
    DLL.insertAfterTailNode(x)

print(DLL.printTheList())
DLL.insertAtPosition(2, 555)
DLL.insertAtPosition(3, 655)

print(DLL.printTheList())
print(DLL.peekHead())
print(DLL.peekTail())
print(DLL.searchForAValue(2))

