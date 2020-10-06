'''
Time O(max(a, b)) | Space O(max(a, b))
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #get length
        l = max(len(a), len(b))
        
        #fill with 0
        a = a.zfill(l); b= b.zfill(l)
        
        #ds to hold values
        ans = []
        carry = 0
        
        for i in range(l-1, -1, -1): #iterate in reverse
            #check for 1 to add to carry
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1
                
            #mod carry by 2 and check remainder
            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')
                
            #divide carry by 2
            carry //= 2
        
        #check if left over carry has 1
        if carry == 1:
            ans.append('1')
            
        #reverse ans
        ans.reverse()
        
        return ''.join(ans)