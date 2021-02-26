class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        sliding window anagram approach. iterate end -> adjust p_dic and matched with right_char -> slide window, undo matched, put back char
        
        time O(s+p) | space O(s at worst for ans)
        '''
        ans = []
        start = 0
        matched = 0
        p_dic = collections.Counter(p)
        
        for end in range(len(s)):
            right_char = s[end]
            
            #decrement p_dic and matched
            if right_char in p_dic:
                p_dic[right_char] -= 1
                
                #complete match of a single char
                if p_dic[right_char] == 0:
                    matched += 1
                    
            #get the index
            if matched == len(p_dic): #p_dic since we only increment matched if character counts are 0
                ans.append(start)
                
            #slide window, undo matched and put back char
            if end >= len(p) -1:
                left_char = s[start]
                
                if left_char in p_dic:
                    if p_dic[left_char] == 0:
                        matched -= 1

                    p_dic[left_char] += 1
                
                start += 1
                
        return ans