class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#         '''
#         using extra space and stack like approach
#         time O(s+t) | space O(s+t)
#         '''
#         s = ""
#         for x in S:
#             if x == "#":
#                 s = s[:-1] # deletes the last character
#             else:
#                 s += x
                
#         t = ""
#         for x in T:
#             if x == "#":
#                 t = t[:-1] # deletes the last character
#             else:
#                 t += x
                
#         return s == t
        
    def backspaceCompare(self, S: str, T: str) -> bool:
        '''
        two pointers left -> right
        for optimized space
        '''
        sidx = len(S)-1
        tidx = len(T)-1
        
        while sidx >= 0 or tidx >= 0: #while either of the indexes have chars to process
            #reduce indexes that need to be deleted
            i1 = self.getNextValidIndex(S, sidx)
            i2 = self.getNextValidIndex(T, tidx)
            
            #if both reached below index 0, we have a match
            if i1 < 0 and i2 < 0: return True
            
            #if either one of them reach below index 0 first, we don't
            if i1 < 0 or i2 < 0: return False
            
            #if characters at l1 and l2 arent same, we dont have a match
            if S[i1] != T[i2]: return False
            
            #set the original indexes to i1-1 and i2-1
            sidx = i1-1
            tidx = i2-1
            
        return True
            
    def getNextValidIndex(self, s, idx):
        backspaceCount = 0
        while idx >= 0:
            if s[idx] == "#": #found a backspace
                backspaceCount += 1
            elif backspaceCount > 0: #found a char that needs to be deleted
                backspaceCount -= 1
            else: #if either of the above don't trigger, then this is good
                break
                
            idx -= 1 #reduce the index for the # and deleted character
            
        return idx