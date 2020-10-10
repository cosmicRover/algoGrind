'''
Time O(n) | Space O(n) for q or on the recursive callsatck
Remember, each node has an alternating set lower and upper boundry that they cant cross
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #base case
        if not root: return True
        
        return self.checkBstRec(root, float("-inf"), float("inf"))
        
    def checkBst(self, root, lower, upper):
        #iterative approach
        
        #since it's alternating, we group the node, lowe and upper together
        
        q = [(root, lower, upper)]
        
        while q:
            node, lower, upper = q.pop()
            if not node: continue
                
            #node's value cant be less than lower bound
            #and node's value cant be more than the upper bound
            if node.val <= lower or node.val >= upper:
                return False
            
            q.append((node.right, node.val, upper))
            
            q.append((node.left, lower, node.val))
            
        return True
    
    def checkBstRec(self, root, lower, upper):
        
        #base case
        if not root: return True
            
        #BST comparison test
        if root.val <= lower or root.val >= upper:
            return False
        
        #right node test
        if not self.checkBstRec(root.right, root.val, upper):
            return False
        
        #left node test
        if not self.checkBstRec(root.left, lower, root.val):
            return False
        
        #retun True if all other tests dont trigger
        return True
            
            
            
            
            
            
            
            
        
        




