import collections

class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list) #import defaultdict for more flexible key storage
        
        for s in strs:
            #init english characters
            count = [0] * 26
            
            #get the ord of the characters, it will form an unique key
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            #store the count as key and the current s as value
            ans[tuple(count)].append(s)
        
        #return the values
        return ans.values()