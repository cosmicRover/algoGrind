from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        sliding window technique. iterate end -> slide start
        
        once we have a dic for pattern, we match with each char we see in string s and adjust p_dic.
        slide the window once end is of sufficient size and put back the adjusted characters
        
        time O(s + p) | space O(s) for each matched index on string s
        '''
        ans = []
        start = 0
        matched = 0
        p_dic = Counter(p)
        
        for end in range(len(s)):
            right_char = s[end]
            
            if right_char in p_dic:
                #matching
                p_dic[right_char] -= 1
                if p_dic[right_char] == 0:
                    matched += 1
            
            #we have a match
            if matched == len(p_dic):
                ans.append(start)
                
            #slide the window
            if end >= len(p) - 1:
                left_char = s[start]
                
                #put the chars back to p_dic
                if left_char in p_dic:
                    #decrement match if no more char remain
                    if p_dic[left_char] == 0:
                        matched -= 1
                    
                    p_dic[left_char] += 1
                    
                start += 1
                
        return ans   