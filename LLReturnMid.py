# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #init root and size counter vars
        size = 0
        root = head
        
        # loop through once to find the size
        while root:
            size += 1
            root = root.next
        
        # loop through once again to get to that position and return it
        newCounter = 0
        while head:
            if newCounter == (size/2):
                return head
            head = head.next
            newCounter += 1
            
        #won't work if list loops


    def middleNodeOnePass(self, head):
        # using slow and fast pointer,
        # fast runs twice as fast as slow
        # and will land in the middle when fast reaches none
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow