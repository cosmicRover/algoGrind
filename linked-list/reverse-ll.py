class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        time O(n)
        
        steps to reverse SLL
        1) have a prev = None
        2) save next
        3) point head.next to prev
        4) set prev to head
        5) set head to saved next before
        
        '''
        return self.reverse(head)
    
    def reverse(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev