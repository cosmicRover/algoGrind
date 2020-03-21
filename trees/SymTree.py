#recursive dfs O(v+E)
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.dfs(root.left, root.right)
        
    def dfs(self, left, right):
        if left and right:
            print(left.val, right.val)
            return left.val == right.val and self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
        
        return left == right