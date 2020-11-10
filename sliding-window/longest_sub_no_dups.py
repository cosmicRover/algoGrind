class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Sliding window start -> end
        The trick is to relaize that if a character already exists in the dic,
        we can just go ahead and jump start to the latest index + 1.
        We save the index of end char to dic, and calculate new longest from the
        max of longest and end-start+1 (aka the disnace of the indexes)
        '''
        
        #init some pointers
        start = 0; longest = 0;
        dic = {}
        
        #traverse the string
        for end in range(len(s)):
            char = s[end]
            
            #if char already exists, adjust the start pointer as max of start and char frequency
            if char in dic:
                start = max(start, dic[char]+1)
                
            #save the right index to dic
            dic[char] = end
            
            #find the longest length
            longest = max(longest, end-start+1)
                
            
        return longest