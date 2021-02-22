from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        sliding window anagram approach.
        '''
        start = 0; matched = 0; sub_start = 0;
        min_length = len(s) + 1 #minimum possible in the worst case
        
        p_dic = Counter(t)
        
        for end in range(len(s)):
            right_char = s[end]
            
            if right_char in p_dic:
                p_dic[right_char] -=1
                
                #count every matching of a character
                if p_dic[right_char] >= 0:
                    matched += 1
                
            #slide windoow and finish as soon as we remove a matched character
            while matched == len(t):
                size = end - start + 1;
                if min_length > size:
                    min_length = min(min_length, size)
                    sub_start = start
                    
                left_char = s[start]
                start += 1
                
                #adjust matched and put back the adjusted char
                if left_char in p_dic:
                    if p_dic[left_char] == 0:
                        matched -= 1
                        
                    p_dic[left_char] += 1
            
        if min_length > len(s): return ""
        
        return s[sub_start:sub_start+min_length]