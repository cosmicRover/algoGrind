class MinPQHeap:
    def __init__(self, array):
        self.items = [0]
        self.buildHeap(array)

    def __len__(self):
        return len(self.items) - 1

    #build the heap the end index thus, siftDown in O(n)
    def buildHeap(self, array):
        index = len(array) // 2
        self.items += array
        
        while index > 0:
            self.siftDown(index)
            index -= 1

    #append a value to the items and expand thus, siftUp in O(log(n))
    def insert(self, val):
        self.items.append(val)
        self.siftUp()

    #brings the smaller values to the left. It is opposite for maxPQ
    def siftUp(self):
        index = len(self)
        
        while index // 2 > 0:
            if self.items[index] < self.items[index // 2]:
                self.swap(index // 2, index, self.items)
            index = index // 2

    #brings smaller values to the left, opposite for maxPQ
    def siftDown(self, index):
        while index * 2 <= len(self):
            mc = self.minChild(index)
            if self.items[index] > self.items[mc]:
                self.swap(index, mc, self.items)
            index = mc

    #get the 1'st elemnt from the index O(1), then siftDown to accomodate O(log(n))
    def getMin(self):
        if len(self.items) < 2:
            return None

        rv = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.siftDown(1)
        return rv

    #compares and return the index of the index of the minValue for minPQ
    #for max, consider returning the max child
    def minChild(self, index):
        if index * 2 + 1 > len(self): 
            return index * 2
        
        if self.items[index * 2] < self.items[index * 2 + 1]: 
            return index * 2

        return index * 2 + 1

    
    def swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]

arr = [45, -2]
bh = MinPQHeap(arr)

print(bh.items)
print(bh.getMin())
print(bh.items)
print(bh.getMin())
print(bh.items)
print(bh.getMin())
print(bh.items)
print(bh.getMin())
print(bh.items)
print(bh.getMin())
print(bh.items)
print(bh.getMin())
print(bh.items)
print(bh.getMin())
print(bh.items)
bh.insert(99)
bh.insert(45)
bh.insert(103)
bh.insert(12)
print(bh.items)
print(bh.getMin())
print(bh.items)