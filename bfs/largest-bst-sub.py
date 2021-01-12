class Solution:
    '''
    this problem combines two other problems but the trick is to validate a subtree beyond 
    root.left and root.right. recursively calling largestBSTSubtree() helps us to tackle 
    that problem as is the key roadblock to just doing it iteratively.
    
    time O(N) since on each step we may end up traversing each node on the tree 
    space O(N) since we may end up storing n nodes
    '''
    
    
    def largestBSTSubtree(self, root: TreeNode) -> int:    
        if not root: return 0
        
        #if the tree itself is BST
        if self.isBST(root, -sys.maxsize, sys.maxsize): 
            return self.count(root)
        
        #recursively calling would allow for validating partial subtree beyond root.left and root.right
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))
    
    #use level order bfs to count nodes
    def count(self, node):
        m = 0
        q = [node]
        
        while q:
            size = len(q)
            m += size
            
            for _ in range(size):
                node = q.pop(0)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return m
    
    #use standard bfs validation to validate a bst
    def isBST(self, node, _min, _max):
        q = [(node, _min, _max)]
        
        while q:
            item, lower, higher = q.pop(0)
            
            if item.val <= lower or item.val >= higher:
                return False
            
            if item.left:
                q.append((item.left, lower, item.val))
                
            if item.right:
                q.append((item.right, item.val, higher))
                
        return True