# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        
        # init vars to the head
        slow = fast = head
        
        # loop the two pointers
        while fast and fast.next:
            # advance slow by one and fast by two
            slow = slow.next
            fast = fast.next.next
            
            # if they match, break out of the loop
            if slow == fast:
                break
        # return None if encountered
        else:
            return None
        
        # advance head and slow till they meet,
        # and then return head
        while head != slow:
            slow = slow.next
            head = head.next
        return head
                