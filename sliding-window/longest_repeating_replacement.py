class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Sliding window start -> end
        The trick here is to figure out when to slide the window as we go through the loop
        if (end-start+1)-repeat > k, thats when we adjust the window
        '''
        start = 0; maxRepeatedCount = 0; maxLength = 0;
        dic = {}
        
        for end in range(len(s)):
            #save the frequency
            char = s[end]
            if char not in dic:
                dic[char] = 0
            dic[char] += 1
            
            #save/repalce the max repeated character count we have seen so far
            maxRepeatedCount = max(maxRepeatedCount, dic[char])
            
            #slide window if necessary
            windowSize = (end-start) + 1
            if (windowSize-maxRepeatedCount) > k: 
                #get hold of the start char and modify dic
                char = s[start]
                dic[char] -= 1
                start += 1
                
            #save the maxLength possible
            maxLength = max(maxLength, end-start+1)
            
        return maxLength