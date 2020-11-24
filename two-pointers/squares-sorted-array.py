class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        '''
        Two pointers left -> right
        The two pointer left, right keeps track of the indexes we need to go through
        and the position index tracks where we must insert the squared value
        Time O(n) | Space O(n)
        '''
        
        left = 0; right = len(A)-1;
        squares = [0] * len(A) #holds the new values
        position = len(A) - 1 #position to assign higher squared value
        
        while left <= right:
            l = A[left]*A[left]
            r = A[right]*A[right]
            
            if l > r:
                squares[position] = l
                left += 1
            else:
                right -= 1
                squares[position] = r
                
            position -= 1
            
        return squares