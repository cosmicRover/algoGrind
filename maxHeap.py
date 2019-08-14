# construction of a maxHeap
# max heap has a top node as the biggest in value

class MaxHeap:

    """
    init with childNodes
    very important to init heap with a value of 0
    for each child node appended, have it siftUp
    """
    def __init__(self, childNodes = []):
        self.heap = [0]
        for node in childNodes:
            self.heap.append(node)
            self.siftUp(len(self.heap) - 1)

    # Time O(log(n))
    # same as __init__, for each insert have the node siftUp
    def insertANode(self, data):
        self.heap.append(data)
        self.siftUp(len(self.heap) -1)

    # Time O(1)
    # returns the current max of the heap, which is stored in index 1
    def peekMaxHeap(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return "Heap is empty"
    
    """
    # Time O(log(n))
    if len(heap) > 2: 
        To pop, first swap the maxHeap with the last element of the heap (len(heap) - 1)
        Then pop the max
        After that siftDown the value where it originally came from

    if len(heap) is 2:
        just pop
    """
    def pop(self):
        if len(self.heap) > 2:
            self.swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.siftDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    # regular python swap
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    """
    # Time O(log(n))
    For siftUp, first get the parent index from the given index,
    if parentIndex turns out <= 1, no need to do anything
    else if the provided heap[index] > heap[parentIndex], swap index with parentIndex 
    and then siftUp the parentIndex. Gets called reccursively till everything is in correct order
    """
    def siftUp(self, index):
        parentIndex = index//2

        if parentIndex <= 1:
            return
        elif self.heap[index] > self.heap[parentIndex]:
            self.swap(index, parentIndex)
            self.siftUp(parentIndex)
    
    """
    # Time O(log(n))
    First calculate the left and the right childNode positions
    """

    def siftDown(self, index):
        left = index * 2
        right = index * 2 + 1

        largest = index

        # determine where the index is supposed to be, left/right
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        
        # if left/right isn't equal to index, we swap first and the call the func recursively
        # with the updated largest index 
        if largest != index:
            self.swap(index, largest)
            self.siftDown(largest)


maxHeap = MaxHeap([5, 6, 14, 55, 8, 2, 4, 7, 9])
print(str(maxHeap.heap[0 : len(maxHeap.heap)]))
maxHeap.pop()
print(str(maxHeap.heap[0: len(maxHeap.heap)]))
print(maxHeap.pop())
print(str(maxHeap.heap[0: len(maxHeap.heap)]))
