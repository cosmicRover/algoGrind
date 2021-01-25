# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        '''
        bst node replacing successor/predecessor approach. successor = node.right's left -> predecessor = node.left's right
        
        time O(log n) | space O(height of tree during recursion)
        '''
        
        
        #find the key
        if not root: return
        
        #while traversing, save root's left and right
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        if root.val == key:
            #leaf node
            if not root.left and not root.right:
                root = None

            #if a right child is present, swap values and replace with successor
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)

            #do the same for left node but with predecessor
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            
            
        return root
            
    #get the leftmost node of root's right
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    #get the rightmost node of node's left
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val