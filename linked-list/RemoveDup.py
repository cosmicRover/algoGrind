'''
Time O(N) | Space O(1)
Two consecutive pointers to splice a linked list
'''


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
        dummy = ListNode(-1)
        dummy.next = head
        
        prev, curr = dummy, dummy.next
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                temp = curr.val
                
                #loop through till unique
                while curr and curr.val == temp:
                    curr = curr.next
                
                #jump back to the previous node after splicing sine current no longer exists
                prev.next = curr
                
            else:
                #keep incrementing with prev and curr
                prev, curr = curr, curr.next
                
        return dummy.next
                