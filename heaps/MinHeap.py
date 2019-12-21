class MinHeap:
    def __init__(self, array):
        print(array)
        
        #globally tracking heap and heap size
        self.heap = [0]
        self.size = 0
        self.buildHeap(array)
        
        print(self.heap)

    #builds the min heap in this class O(lon(n))
    def buildHeap(self, array):
        index = len(array) >> 1

        self.size = len(array)
        self.heap += array[:]
        
        #go downwards 
        while index > 0:
            self.siftDown(index)
            index -= 1

    def siftDown(self, index):
        while index * 2 <= self.size:
            child = self.getChild(index)
            
            #if current indes's value > child's value, swap.
            if self.heap[index] > self.heap[child]:
                temp = self.heap[index]
                self.heap[index] = self.heap[child]
                self.heap[child] = temp
            index += child # jump to child

    #returns index that is twice the original index as per tree child
    def getChild(self, index):
        if index * 2 + 1 > self.size: return index * 2 #checks if can go out of bounds
        
        else: #compares heap values and returns the smaller
            if self.heap[index * 2] < self.heap[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def getMin(self):
        return_val = self.heap[1] # the val to return as the min of the heap
        self.heap[1] = self.heap[self.size] # swap the 1st element with the last

        #decrement size and pop the last element
        self.size -= 1
        self.heap.pop()

        #sift the tree down to readjust for the removed element. siftDown index 1
        self.siftDown(1)
        return return_val

    def insertValue(self, val):
        #insert and inc size
        self.heap.append(val)
        self.size += 1

        #sift tree upwards for increased elments 
        self.siftUp(self.size)

    def siftUp(self, index):
        while index * 2 > 0:
            # if the last appended element is less than it's parent, swap
            if self.heap[index] < self.heap[index // 2]:
                temp = self.heap[index // 2]
                self.heap[index // 2] = self.heap[index]
                self.heap[index] = temp
            index = index // 2 # decrement backwards to the parent (parent = index // 2)


array = [3, 5, 6, 1, 2, -6, 33, 65, 78, -99, 0, 88]
min_heap = MinHeap(array)
print(min_heap.getMin())
print(min_heap.heap)
print(min_heap.getMin())
print(min_heap.heap)
print(min_heap.getMin())
print(min_heap.heap)
print(min_heap.getMin())
print(min_heap.heap)
# min_heap.insertValue(55)
# print(min_heap.heap)
# print(min_heap.getMin())
# print(min_heap.getMin())
# print(min_heap.heap)
# print(min_heap.getMin())
# min_heap.insertValue(-999)
# print(min_heap.getMin())
# print(min_heap.heap)
