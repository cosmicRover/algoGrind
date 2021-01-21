# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        '''
        linked list jumping off each other approach.
        [1][2][3][4][5][6]
        odd's next will be even
        even's next will be odd
        '''
        if not head: return
        
        #prep the pointers
        odd = head
        even = head.next
        
        #save a head for even
        evenHead = even
        
        #jumping off each pointer approach
        #iterate on even and even.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        #connect odd with even
        odd.next = evenHead
        
        return head