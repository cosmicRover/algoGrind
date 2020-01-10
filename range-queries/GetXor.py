'''
range queries are perfectly suited for segment tree/fenwick tree
Below is an example of taking the tree aspect of fenwick tree
and calculating accumulated xor beforehand to perform range xor
queries more efficiently.
precompute values -> perform queries
'''

class Solution:
    
    # time O(n) space O(n+1)
    def xorQueries(self, arr: [int], queries: [[int]]) -> [int]:
        tree = [0] * (len(arr) + 1)
        r = []
        
        #build the tree, pre-compute the accumulated xor 
        for i, v in enumerate(arr):
            tree[i+1] = self.getxor(tree[i], v) #if change ^ to +, you get accumulated sum of elements in index
        
        #go through the query pairs, and append the xored values from the pre-computed tree
        for x, y in queries:
            r.append(self.getxor(tree[x], tree[y+1]))
            
        return r
    
    def getxor(self, num, num2):
        return num ^ num2