#a lesson in hash table
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        #store freq O(n)
        dic = {}
        for x in s:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
                
        #find the first key with value 1, if found: find it's index from s O(n)
        for x in dic:
            if dic[x] == 1:
                return s.index(x) # -> O(n)
        else:
            return -1