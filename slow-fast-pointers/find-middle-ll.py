# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
        slow/fast pointer approach. slow.next -> fast.next.next
        exact same approach finding a cycle in LL
        time O(n) | space O(1)
        '''
        
        slow = fast = head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow