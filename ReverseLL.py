# Problem leetCode SinglyLL and SinglyLL 2


class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.nextNode = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def peekHead(self):
        return self.head

    def appendANode(self, newNode):
        if self.head is None:
            self.head = Node(newNode)
            return
        
        currentNode = self.head

        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = Node(newNode)

    def getAllNodes(self):

        currentNode = self.head
        children = []

        while currentNode:
            children.append(currentNode.data)
            currentNode = currentNode.nextNode
        
        return children

    def findANode(self, nodeToFind):
        currentNode = self.head

        while currentNode:
            if currentNode.data == nodeToFind:
                return True
            else:
                currentNode = currentNode.nextNode
        return False

    def reverseSinglyLinkedList(self):

        #init the vars
        previous = None
        currentNode = self.head
        next = currentNode.nextNode

        #loop till current is None
        while currentNode:

            #set current's nextNode to previous
            currentNode.nextNode = previous

            #previous becomes the currentNode and currentNode to next
            previous = currentNode
            currentNode = next

            # if next exists, set next to it's nextNode
            if next:
                next = next.nextNode
        #init head
        self.head = previous


    def reverseSinglyLinkedListFromMtoN(self, head, initialPosition:int, endingPosition:int):

        # init as Node variables
        previousNode = dummyNode = Node(None)

        #just stores a refference to the head that was passed
        dummyNode.nextNode = head 
        
        #init a tailNode to keep track of the nextNode
        tailNode:Node

        # traverse to the starting position of the subList
        for _ in range(initialPosition-1):
            previousNode = previousNode.nextNode
            tailNode = previousNode.nextNode

        for _ in range(endingPosition - initialPosition):
            tempNode = previousNode.nextNode # start of the sublist i.e. initialPosition
            previousNode.nextNode = tailNode.nextNode #switch out the prev's nextNode with tail's nextNode
            tailNode.nextNode = tailNode.nextNode.nextNode # set tail's nextNode by 1 to the right
            previousNode.nextNode.nextNode = tempNode # set prev's next's next to the tempNode we created before
        return dummyNode.nextNode # return the headNode if necessary

    #reconnects the nextPointers to get rid of node
    def removeANode(self, nodeToRemove):

        currentNode = self.head

        while currentNode.nextNode:
            if currentNode.nextNode.data == nodeToRemove:
                print("found the node")

                currentNode.nextNode = currentNode.nextNode.nextNode

            currentNode = currentNode.nextNode




LL = SinglyLinkedList()
array = [4, 5, 6, 7, 8, 9, 10, 11, 12]
for x in array:
    LL.appendANode(x)

print(LL.getAllNodes())
#LL.reverseSinglyLinkedListFromMtoN(LL.head, 4, 8)
#print(LL.getAllNodes())
LL.removeANode(10)
print(LL.getAllNodes())

