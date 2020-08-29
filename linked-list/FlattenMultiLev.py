'''
Since this problem requires graph like traversal, using a stack is suitable
Time O(N) | Space O(N)
'''

class Solution:
    def flatten(self, head):
        if not head: return head
        
        #stack based approach
        stack = [head]
        ans = []
        
        while stack:
            
            item = stack.pop()
            ans.append(item) #storing the nodes in an array
            
            #we need to append the next and children onto the stack, but children last
            if item.next:
                stack.append(item.next)
            if item.child:
                stack.append(item.child)
                
        #time to reattach the nodes on next and prev, remove child
        #since we are storing them as an array, it is versatile to use range index
        
        for i in range(len(ans) -1):
            head = ans[i]
            next = ans[i+1]
            
            head.next = next
            next.prev = head
            head.child = None
            
            
        return ans[0]