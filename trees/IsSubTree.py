'''
P   NLR
I   LNR
PO  LRN
'''

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t or not s: return
        
        first = self.treeTrav(s)
        second = self.treeTrav(t)
        
        print(first, "___", second)
        
        return second in first
        
    #post order
    def treeTrav(self, node):
        if not node:
            return None
        
        # transform values into text on the go f" your_text {functionCall} "
        return f"node{node.val} {self.treeTrav(node.left)} {self.treeTrav(node.right)}"
    