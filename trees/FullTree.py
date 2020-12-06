class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        '''
        Full tree: The tree is left leaning. Meaning that all the nodes
        have left node before they have a right node. Otherwise it's invalid.
        When we encounter a None node, we can't encounter any other node afteewards 
        '''
        q = [root]
        hasNone = False
        
        while q:
            node = q.pop(0)
            if not node:
                hasNone = True
            
            if hasNone and node:
                return False
            
            if node:
                q.append(node.left)
                q.append(node.right)
            
        return True