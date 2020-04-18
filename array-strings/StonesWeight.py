'''
Stones weight

Time O(nlogn) due to merge sort can be done in O(n) without sort
Space O(n) due to merge sort

'''


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while stones:
            if len(stones) <= 1:
                return stones.pop()
            
            self.merge(stones)
            
            y = stones.pop()
            x = stones.pop()
            
            if x == y: 
                continue
                
            else:
                y = y - x
                stones.append(y)
        
        else: return 0
        
    
    def merge(self, arr):
        '''
        M D R M F L
        '''
        
        if len(arr) > 1:
            mid = len(arr) // 2
        
            left = arr[:mid]
            right = arr[mid:]
        
            self.merge(left)
            self.merge(right)
            
            arr.clear()
            
            while left and right:
                if left[0] <= right[0]:
                    item = left.pop(0)
                    arr.append(item)
                    
                else:
                    item = right.pop(0)
                    arr.append(item)
                    
            for i in left:
                arr.append(i)
                
            for j in right:
                arr.append(j)