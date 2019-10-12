#leetcode 236
# use a hastab to remember parents
# use dfs to traverse
# use a set later to backtrack from given nodes to it's parents


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self, root, p, q):
        
        #the hash will keep track of each node's parent node
        parentTable = {root: None}
        stack = [root]
        
        while p not in parentTable or q not in parentTable:
            node = stack.pop()
            
            if node.left:
                # insert to parent table and append to satck
                parentTable[node.left] = node
                stack.append(node.left)
            
            if node.right:
                parentTable[node.right] = node
                stack.append(node.right)
                
        #create a set to  backtrack from node --> parent
        ancestors = set()
        
        #while p isn't None, add the parent to the ancestors
        #backtrack from node --> parent
        while p:
            print(p.val)
            ancestors.add(p)
            p = parentTable[p]
            
        print("-----")
        
        #backtrack from node --> parent
        while q not in ancestors:
            print(q.val)
            q = parentTable[q]
            
        print("the last iteration of q is the answer -> ", q.val)
        
        return q
        
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.dfs(root, p, q)
        
        
        
        
        
        
        