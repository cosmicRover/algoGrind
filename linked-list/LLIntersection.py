'''
Time O(N) | Space O(N)
'''


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB: return
        
        a, b = headA, headB
        visited = set()
        
        while a:
            visited.add(a) 
            a = a.next
            
        while b:
            if b in visited:
                return b
            
            visited.add(b) 
            b = b.next