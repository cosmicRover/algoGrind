# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        The tricky part is alternating between two heads 
        second.next, second = first, second.next
        first.next, first = second, first.next
        
        time O(n) | space O(1)
        
        """
        if not head: return
        
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        first_half = head
        second_half = self.reverse(slow)
        
        #this is the tricky part, alternating in place. Must swap in one go!
        while second_half.next: #we only care while second_half has nodes
            
            #attach first.next to second and increment first to first.next
            first_half.next, first_half = second_half, first_half.next
            
            #attach second.next to first and increment second to second.next
            second_half.next, second_half = first_half, second_half.next
   
    def reverse(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev