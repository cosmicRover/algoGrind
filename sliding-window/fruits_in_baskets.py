'''
Time O(n) | Space O(1) since there can be only a max of 3 distinct types of keys in dic
'''

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        '''
        Sliding window. start -> end
        
        constarints: 2 baskets, 1 type in each
        [0, 1, 2, 2]
        '''
        
        start = 0; maxAmt = float("-inf");
        dic = {}
        
        for end in range(len(tree)):
            #save the counts
            s = tree[end]
            if s not in dic:
                dic[s] = 0
            dic[s] += 1
            
            #slide the windows
            while len(dic) > 2:
                #reduce/delete the dic element
                s = tree[start]
                dic[s] -= 1
                if dic[s] == 0:
                    del dic[s]
                    
                #slide start to the right
                start += 1
            
            #save the maximum amount from baskets
            val = 0
            for x in dic:
                val += dic[x]
            maxAmt = max(maxAmt, val)
            
        return maxAmt
        