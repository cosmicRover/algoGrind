class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        sdict ={}
        tdict = {}
        
        for x in s:
            if x not in sdict: sdict[x] = 1
            else: sdict[x] += 1
                
        for x in t:
            if x not in tdict: tdict[x] = 1
            else: tdict[x] += 1
                
        return sdict == tdict