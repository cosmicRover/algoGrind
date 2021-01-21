# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        reverse ll approach with q-p+1 reverse algorithm
        
        time O(n) | space O(1)
        '''
        if m==n: return head
        
        #prep pointers
        prev = None
        current = head
        count = 0
        
        #get m'th and m-1 node
        while current and count < m-1: #m-1 will prevent us from over stepping
            prev = current
            current = current.next
            count += 1
            
        #save pointers to left and right side
        left_side = prev
        right_side = current
        
        #reverse using q-p+1 algorithm
        #pointer prep
        count = 0
        next = None
        
        while current and count < n-m+1:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
            
        #conenct the left and right side
        if left_side:
            left_side.next = prev
        else:
            head = prev
            
        right_side.next = current
        return head