'''
Time O(len(s) + (num of time we adjust minLen)) | Space O(len(s))
The sliding window technique is where we use two pointers to adjust
a minimum elemnts required in a DS to achieve the desired output
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        
        #init a hash for every characters in s and hash t
        need = {char: 0 for char in s}   
        for x in t:
            if x in need: need[x] += 1
            else: need[x] = 1
                
        count, minLen, start, end = 0, float("inf"), -1, -1
        left = right = 0
        
        while right < len(s):
            #if we encounter a t match on need, inc count
            if need[s[right]] > 0:
                count += 1
            
            #dec need value to indicate that we dont need it
            need[s[right]] -= 1
            
            #if we matched everything
            if count == len(t):

                #readjust left and bring dict values back to 1
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                #readjust minLen, start and end 
                if minLen > right - left +1:
                    minLen = right - left + 1 #remembers the minLen necessary for output
                    start = left
                    end = right + 1 #being inclusive
                
                #increment for first postion since the loop abobe will stop there
                need[s[left]] += 1
                left += 1
                count -= 1
            
            right +=1
                
        return "" if start == -1 else s[start: end]
            