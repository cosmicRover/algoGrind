class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        array representation of a tree. use a stack to travers the tree
        but when there is a valid node, append left and right side to the stack
        but only append the value of the node to arr. If not a valid node, append
        None instead
        
        time O(n where n is the amx size of a tree) | space O(n) 
        '''

        p = self.arrRep(p)
        q = self.arrRep(q)

        return p == q

    def arrRep(self, root):
        #array representation of a given tree
        stack = [root]
        result = []

        while stack:
            node = stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)
                result.append(node.val)
            else:
                result.append(None)

        return result
