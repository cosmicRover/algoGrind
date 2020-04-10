'''
Time O(2n) => O(n) | Space(n) for the dic
'''
class Solution:
    def countElements(self, arr: [int]) -> int:
        if len(arr) <= 1: return 0
        
        dic = {}
        for x in arr:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1   
                
        hit = 0
        for x in arr:
            val = x +1
            
            if val in dic:
                hit += 1
                
        return hit