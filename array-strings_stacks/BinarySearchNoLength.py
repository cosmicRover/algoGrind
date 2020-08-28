# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        jump = 0
        
        while jump != -1:
            val = reader.get(jump)
            
            if val == target: return jump
            
            #keep jumping until we find a suitable window. Can even be a thousand
            elif target > val:
                jump += 100
            
            elif target < val:
                # binary search in this window
                start = 0
                end = jump
                
                while start <= end:
                    mid = (end+start)//2
                    val = reader.get(mid)
                    
                    if target == val:
                        return mid
                    elif target > val:
                        start = mid + 1
                    elif target < val:
                        end = mid - 1
                else:
                    return -1
                    
        else: return -1