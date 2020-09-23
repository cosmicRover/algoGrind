# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        self.depth(root)
        return self.ans-1
    
    #dfs approach to depth calculating
    def depth(self, node):
        if not node: return 0
        
        #recursively call left and right
        left = self.depth(node.left)
        right = self.depth(node.right)
        
        #stre the max between "not passing through root" vs "passing through root"
        self.ans = max(self.ans, left+right+1)
        return max(left, right) + 1 #gotta increment by 1 on recursive callstack