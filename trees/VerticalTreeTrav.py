Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self,root):
        
        #ds to store the markings as a list of objects with key
        dic = collections.defaultdict(list)
        
        #stack with node, row, col tuple
        stack = [(root, 0, 0)] #starting at root is 0, 0
        
        #binary tree level order with len() technique + Post-order
        
        while stack:
            for _ in range(len(stack)):
                
                #pop an item
                node, row, col = stack.pop()
                
                #save the row, col, and node as dic[row].append(col, node.val). Unrelated to stack
                dic[row].append((col, node.val))
                
                #append the children in post-order technique, but modify the row, col. col is always col-1
                if node.left:
                    stack.append((node.left, row-1, col-1))
                if node.right:
                    stack.append((node.right, row+1, col-1))
                
        ans = []
        
        #sort the dic keys and valus and return them
        for key in sorted(dic.keys()):
            level=[x[1] for x in sorted(dic[key], key=lambda x:(-x[0],x[1])) ] #sort each dic row by the value
            ans.append(level)
            
        return ans