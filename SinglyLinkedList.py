class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.nextNode = None

    def setNext(self, next):
        self.nextNode = next

    def getData(self):
        return self.data

class LinkedList(object):

    def __init__(self):
        self.head = None

    def peekHead(self):
        return self.head.data

    def setHead(self, data):
        self.head = Node(data)

    # add a new node
    def appendToList(self, data):

        current = self.head

        if current is None:
            self.setHead(data)
            return

        while current.nextNode:
            current = current.nextNode
        current.nextNode = Node(data)
        
    # get all the children
    def getChildren(self):

        children = []

        current = self.head

        if current is None:
            print("LL is empty")
            return

        while current:
            children.append(current.data)
            current = current.nextNode
        return children



LL = LinkedList()
LL.appendToList(5)
LL.appendToList(6)
LL.appendToList(7)

print(LL.getChildren())


        

    

    
