import heapq


class MedianFinder:

    def __init__(self):
        """
        two heaps approach. create two heaps -> maintain balance
        
        time O(n log n) | space O(n)
        """
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        #step 1, append to heap
        if not self.left or -self.left[0] > num:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        #step 2, balance the heaps
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))

        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        #if the length is equal, median will be the 0th  index of both values
        if len(self.left) == len(self.right):
            return (-self.left[0]+self.right[0])/2

        #otherwise median is the 0th index of left heap
        return -self.left[0]/1
