class Solution:
    def deleteNode(self, root, key):
        if not root:
            return
        
        #traverse left or right based on BST property
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        else: #found a match
            # if the subtree does not have a left child, we just return its right child
            # to its father, and they will be connected on the higher level recursion.
            if not root.left:
                return root.right
            
            # if it has a left child, we want to find the max val on the left subtree to 
            # replace the node we want to delete.
            else:
                # find the rightmost value of left sub tree
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                    
                # replace the values
                root.val = tmp.val
                
                # since we have replaced the node we want to delete with the tmp, now we don't
                # want to keep the tmp on this tree, so we just use our function to delete it.
                # pass the val of tmp to the left subtree and repeat the whole approach.
                root.left = self.deleteNode(root.left, tmp.val)
        
        return root

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        