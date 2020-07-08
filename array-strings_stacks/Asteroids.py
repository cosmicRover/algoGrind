'''
Time O(N) | Space O(N)
The trick is to keep employ a stack and keep checking the latest item on the stack against the 
'''

class Solution(object):
    def asteroidCollision(self, asteroids):
        
        ans = []
        
        for new in asteroids:
            
            while ans and new < 0 < ans[-1]: #checking for a direction conflict
            
                if abs(ans[-1]) < abs(new):
                    ans.pop() #keep popping the lst item from answer and continue t next iteration
                    continue
                
                elif abs(ans[-1]) == abs(new): #if they are same, no need to append anything
                    ans.pop()
                
                break #break out of the loop once the necessary adjustements have been made
            
            
            else:
                ans.append(new) #append the new item to answer
        
        
        return ans