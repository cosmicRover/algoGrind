#crucial tree trav question, important thing to keep in mind that in each level of the tree,
#we must call remove method recursively on both left and right subtree

class Solution:
    def removeLeafNodes(self, root, target: int):
        return self.postTrav(root, target)
        
    def postTrav(self, node, target):
        if node == None:
            return None
        
        #must call trav recusrively to get to the leaf node
        node.left = self.postTrav(node.left, target)
        node.right = self.postTrav(node.right, target)
        
        #deleteing the target node by simply returning None to the recursive callstack
        if node.val == target and node.left == None and node.right == None:
            print('found')
            return None
            
        return node