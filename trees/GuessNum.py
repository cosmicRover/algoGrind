# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

'''
Time O(log(n)) | Space O(1)
Standard binary search
'''

class Solution:
    def guessNumber(self, n: int) -> int:
        
        #binary search to navigate higher/lower boundaries
        
        left = 1
        right = n
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if guess(mid) == 1: #if higher
                left = mid + 1
            
            elif guess(mid) == -1: #if lower
                right = mid - 1
                
            elif guess(mid) == 0:
                return mid
        
        return 1