from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #gonna use rolling hash algo to match a substring
        #get the frequencies of s and p
        scount = Counter(s[:len(p)]) #only save till the len(p) index in the begining
        pcount = Counter(p)
        
        ans = []
        
        #if they both eqaul in the begining, we have a match
        if scount == pcount:
            ans.append(0)
        
        #the comparison loop
        for i in range(len(s)-len(p)):
            #del/decrement scount
            
            if scount[s[i]] == 1:
                del scount[s[i]]
            elif scount[s[i]] > 1:
                scount[s[i]] -= 1
                
            #save new characters
            if s[i+len(p)] in pcount:
                scount[s[i+len(p)]] += 1
            else:
                scount[s[i+len(p)]] = 1
                
            if scount == pcount:
                ans.append(i+1)
                
        return ans