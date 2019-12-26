#example of MaxPQ using a Max Heap

class MaxPQHeap:
    def __init__(self, array):
        self.items = [0]
        self.buildHeap(array)

    def __len__(self):
        return len(self.items) - 1

    def buildHeap(self, array):
        index = len(array) // 2
        self.items += array
        while index > 0:
            self.siftDown(index)
            index -= 1

    def insert(self, val):
        self.items.append(val)
        self.siftUp()

    def siftUp(self):
        index = len(self)
        
        while index // 2 > 0:
            if self.items[index] > self.items[index // 2]:
                self.swap(index // 2, index, self.items)
            index = index // 2

    def siftDown(self, index):
        while index * 2 <= len(self):
            mc = self.maxChild(index)
            if self.items[index] < self.items[mc]:
                self.swap(index, mc, self.items)
            index = mc

    def getMax(self):
        if len(self.items) < 2:
            return None

        rv = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.siftDown(1)
        return rv

    def maxChild(self, index):
        if index * 2 + 1 > len(self): 
            return index * 2
        
        if self.items[index * 2] > self.items[index * 2 + 1]: 
            return index * 2

        return index * 2 + 1

    
    def swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]

arr = [45, -2, 55, 999, 12, 0, -32, 55]
bh = MaxPQHeap(arr)

print(bh.items)
print(bh.getMax())
print(bh.items)
print(bh.getMax())
print(bh.items)
print(bh.getMax())
print(bh.items)
print(bh.getMax())
print(bh.items)
bh.insert(34)
bh.insert(22)
bh.insert(103)
print(bh.items)
print(bh.getMax())
print(bh.items)
print(bh.getMax())
print(bh.items)
print(bh.getMax())
print(bh.items)
