# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        copy the next node's value and keep a pointer to the previous node
        
        time O(N) at worst case | space O(1)
        """
        prev = None
        while node.next:

            node.val = node.next.val

            prev = node
            node = node.next

        #set previou node's next node to none as it will be the second to last node
        prev.next = None