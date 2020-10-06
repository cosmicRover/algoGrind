# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #record the parents
        parents = {root:None}
        
        #since this is a bst, we find p, q using bst idea
        self.findNode(root, p, parents)
        self.findNode(root, q, parents)
        
        #stores parents of a given node
        ancestors = set()
        
        #save all the parents
        while p:
            ancestors.add(p)
            p = parents[p]
            
        #match with q
        while q not in ancestors:
            q = parents[q]   
        return q
        
    #BST traversal
    def findNode(self, root, node, parents):
        q = [root]
        while q:
            n = q.pop()
            if n.val==node.val:
                break
            if node.val > n.val and n.right:
                q.append(n.right)
                parents[n.right] = n
            elif node.val < n.val and n.left:
                q.append(n.left)
                parents[n.left] = n