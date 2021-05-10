import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        '''
        find the lowest two value, add them, and put back on heap
        
        time O(n log n) | space O(n)
        '''
        cost = 0
        h = []

        for i in sticks:
            heapq.heappush(h, i)

        while h:
            item1 = heapq.heappop(h)

            if not h:
                break

            item2 = heapq.heappop(h)

            val = item1 + item2
            cost += val

            heapq.heappush(h, val)

        return cost
