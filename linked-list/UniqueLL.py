# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first, second = head, head.next if head else None
        
        while second:
            if first.val == second.val:
                #manually override a link with the next property
                #aka the squash method
                second = second.next
                first.next = second
            
            else:
                first = second
                second = second.next
                
        
        return head
                    