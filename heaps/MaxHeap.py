class MaxHeap:
    def __init__(self, array):
        print(array)
        self.heap = [0]
        self.size = 0
        self.buildHeap(array)
        print(self.heap)

    def buildHeap(self, array):
        index = len(array) // 2

        self.size = len(array)
        self.heap += array[:]

        while index > 0:
            self.siftDown(index)
            index -= 1

    def siftDown(self, index):
        while index * 2 <= self.size:
            child = self.getChild(index)
            
            #if current indes's value < child's value, swap.
            if self.heap[index] < self.heap[child]:
                temp = self.heap[index]
                self.heap[index] = self.heap[child]
                self.heap[child] = temp
            index += child # jump to child

    def getChild(self, index):
        if index * 2 + 1 > self.size: return index * 2

        else:
            if self.heap[index * 2] > self.heap[index * 2 +1]:
                return index*2
            else:
                return index * 2 + 1

    def getMax(self):
        temp = self.heap[1]

        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.siftDown(1)
        print(self.heap)
        return temp

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.siftUp(self.size) #expand on the established size

    def siftUp(self, index):
        while index * 2 > 0:
            #if child > parent
            if self.heap[index] > self.heap[index // 2]:
                temp = self.heap[index // 2]
                self.heap[index // 2] = self.heap[index]
                self.heap[index] = temp
            index = (index - 1) // 2






array = [3, 5, 6, 1, 2, -6, 0, 33, 65, 98, -99, 0, 88]
max_heap = MaxHeap(array)
print(max_heap.getMax())
print(max_heap.heap)
print(max_heap.getMax())
print(max_heap.getMax())
# max_heap.insert(99)
# print(max_heap.heap)
# print(max_heap.getMax())
# print(max_heap.heap)
# print(max_heap.getMax())