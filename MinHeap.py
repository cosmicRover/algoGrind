# Problem M 16
# Solution
# heaps are useful when keeping track of lowest/highest values

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # Time O(n) | O(1) space
    def buildHeap(self, array):

        # firstParentIdx is always -2 before rounding and dividing by 2
        firstParentIdx = (len(array) - 2) // 2
        
        # placement starts from the end of the array
        for currentIdex in reversed(range(firstParentIdx)):
            self.siftDown(currentIdex, len(array) - 1, array)
        return array

    # Time O(Log(n)) | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1

            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break

    # Time O(Log(n)) | O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    # Time O(1)
    def peek(self):
        return self.heap[0]

    # Time O(Log(n)) | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) -1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    # Time O(Log(n)) | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[i], heap[j]

