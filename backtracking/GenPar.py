'''
Intro to backtrack. 
Choice
Constraints
Goal

Time and space O(4^n/sqrt(n))
'''

class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        return self.backtrack('', 0, 0, n, [])
    
    def backtrack(self, s, left, right, n, arr):
        
        #if we reach the goal, we append
        if len(s) == 2 * n:
            arr.append(s)
            return
        
        #permutation branches
        if left < n:
            self.backtrack(s+'(', left+1, right, n, arr)
            
        if right < left:
            self.backtrack(s+')', left, right+1, n, arr)
            
        return arr