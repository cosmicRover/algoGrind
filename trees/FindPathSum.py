'''
Note that the path sum has to reach the bottom to be considered.
Time O(N) | Space O(N) for the recursive call space
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root: return False

        #instead of having an extra var to keep of sum, you can
        #just subtract the val from the sum in the hopes you get a 0
        sum -= root.val 
            
        #if no brnach left, look for sum to be 0
        #Path sum requires this
        if not root.right and not root.left:
            return sum == 0
            
        return self.hasPathSum(root.right, sum) or self.hasPathSum(root.left, sum)