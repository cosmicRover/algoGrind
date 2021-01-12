class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        bfs approach. need to balance the left and right brackets
        
        time O(n * 2^n) since we can have a max of 2^n balanced brackets as combinations and concatenating s takes n time
        space O(n * 2^n)
        '''
        
        results = []
        q = [("", 0, 0)] #start with empty and left, right brackeyt numbers
        
        while q:
            s, l, r = q.pop(0)
            
            if l == n and r == n:
                results.append(s)
                
            else:
                #make decisions on what bracket to add
                #left compares with n
                if l < n:
                    q.append((s+"(", l+1, r))
                
                #right compares with left
                if r < l:
                    q.append((s+")", l, r+1))
                    
        return results