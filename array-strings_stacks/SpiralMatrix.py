'''
This problem is easy to visualize but the concept of shrinking box, along with
matrix bounds needs to be checked properly before it can be implemented

Time O(N) Space | O(N) for the ans array
'''

class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix: return 
        
        ans = []
        
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        
        while left < right and top < bottom:
            #traverse from left to right on top
            for i in range(left, right):
                ans.append(matrix[left][i])
                
            #traverse from right to bottom on right side
            for i in range(top, bottom):
                ans.append(matrix[i][right])
                
            #traverse from left to right at the bottom (hint:backwards)
            for i in range(right, left, -1):
                ans.append(matrix[bottom][i])
                
            #traverse from bottom to up on the left backwards
            for i in range(bottom, top, -1):
                ans.append(matrix[i][left])
                
            #dec/inc the boundary
            top += 1
            left += 1
            right -= 1
            bottom -= 1
        
        #edge cases
        # gets the last square that is left-over
        if left == right and top == bottom:
        	ans.append(matrix[top][left])
            
        #a vertical line 
        elif left == right:
            for i in range(top, bottom+1):
                ans.append(matrix[i][left])
                
        #a horizontal line 
        elif top == bottom:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
                
        
        return ans