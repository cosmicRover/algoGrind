class MaxHeap:
    def __init__(self):
        self.heap = []

    def buildHeap(self):
        for x in self.heap:
            self.insert(x)

    def getParent(self, index):
        return index -1 // 2
    
    def getLeftChild(self, index):
        return 2*index+1
    
    def getRightChild(self, index):
        return 2*index+2

    def hasParent(self, index):
        return self.getParent(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChild(index) < len(self.heap)
    
    def hasRightChild(self, index):
        return self.getRightChild(index) <len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

    def siftUp(self, index):
        size = len(self.heap)
        while self.hasParent(index) and self.heap[index] > self.heap[self.getParent(index)]:
            self.swap(index, self.getParent(index))
            index = self.getParent(index)
    
    def popMax(self):
        if len(self.heap) == 0: return None

        lastIndex = len(self.heap) - 1
        self.swap(0, lastIndex)
        root = self.heap.pop()
        self.siftDown(0)
        return root

    def siftDown(self, index):
        while self.hasLeftChild(index):
            maxChild = self.getMaxChildIndex(index)
            if maxChild == -1 : 
                break
            print("index -->", index, "max child -->>", maxChild)
            if self.heap[index] < self.heap[maxChild]:
                self.swap(index, maxChild)
                index = maxChild
            else:
                break

    def getMaxChildIndex(self, index):
        if self.hasLeftChild(index):
            left = self.getLeftChild(index)
            # print("max")
            if self.hasRightChild(index):
                right = self.getRightChild(index)
                if self.heap[left] > self.heap[right]:
                    return left
                else:
                    return right
        else:
            return -1

inputArr = [76, 2, 3, 11, -9, 3, 0, 4, 11, 99, 103]
mh = MaxHeap()

for x in inputArr:
    mh.insert(x)

print(mh.heap)
print(mh.popMax())
# print(mh.popMax())
# print(mh.popMax())
# print(mh.popMax())
print(mh.heap)