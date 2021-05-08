# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        swap nodes in k elements approach. outer loop -> save pointers -> reverse while i < k -> reconnect left/right -> connect prev to left
        '''
        prev = None
        curr = head

        #outer loop
        while True:

            #save pointers
            left_prev = prev
            left_head = curr

            #reverse while i < k
            i = 0
            next = None

            while curr and i < 2:  # sappwing in pairs, switch k with 2
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                i += 1

            #reconnect left and right
            if left_prev:
                left_prev.next = prev
            else:
                head = prev

            left_head.next = curr

            if not curr:
                break

            prev = left_head

        return head
