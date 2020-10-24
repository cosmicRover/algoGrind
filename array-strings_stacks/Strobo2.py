'''
The trick here is to make some obserbations:
we ONLY permutate strogo numbers with their counterparts
for example: we permutate 6 with 9, 8 with 8, 1 with 1, and 0 with 0
we dont want to permutate starting with 0, and we don't permutate further 
once start==end and we encounter a 6 or 9

Time O(???) | Space O(n where n is the length of total permutation of strobos)
'''


class Solution:
    def findStrobogrammatic(self, n):
        result = []
        hash = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        self.helper(result, [-1]*n, 0, n-1, hash)
    
        return result
    
    def helper(self, result, arr, start, end, hash):
        #when start > end, our permutation is complete
        if start > end:
            result.append(''.join(arr))#we append as a string by joining arr
            return
    
        for key in hash:
            #this to prevent more permutation after encountering a 6 or 9
            if start == end and key in ('6','9'):
                continue
            
            #this to prevent 0 prefix permutation
            if start != end and start == 0 and key == '0':
                continue
            
            #assign key and val with start and end
            arr[start], arr[end] = key, hash[key]
            
            #shrink assign area with each recursive call
            self.helper(result, arr, start+1, end-1, hash)