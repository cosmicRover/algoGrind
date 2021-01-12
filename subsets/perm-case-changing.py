class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        '''
        permutation with case changing using susets method
        copy list -> modify case -> append[i]
        '''
        
        result = [S]
        
        for i in range(len(S)):
            if S[i].isalpha() == False:
                continue
                
            size = len(result)
            
            #copy list -> modify -> append
            for j in range(size):
                copy = list(result[j])
                
                #modify only index i
                copy[i] = self.switchCase(S[i])
                
                #append[i]
                val = "".join(copy)
                result.append(val)
                
        return result
            
    def switchCase(self, c):
        if c.isupper() == True:
            return c.lower()
        else:
            return c.upper()