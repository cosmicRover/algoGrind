from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        sliding window start -> end
        We don not need to permutate s1, as we can use a hash table to keep track of the frequencies
        of the pattern s1 so we can use sliding window to try and match both the pattern and string frequencies
        '''
        
        pCount = Counter(s1) #can optimize this but I suspect this is using O(1) extra memory anyway since maxLength is 26
        start = 0; dic = {};
        
        for end in range(len(s2)):
            #save frequency
            char = s2[end]
            if char not in dic:
                dic[char] = 0
            dic[char] += 1
            
            #check if dic contains more frequency than the pattern. If so, slide window
            while dic[char] > pCount[char]:
                sChar = s2[start]
                dic[sChar] -= 1
                start += 1
            
            #delete the keys that dont have a frequency
            if dic[char] == 0:
                del dic[char]
            
            #pattern permutation check
            if dic == pCount:
                return True
            
        return False