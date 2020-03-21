# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Time O(n) | O(n) space
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val = []
        length = 0
        
        while head:
            node = head
            val.append(node.val)
            head = head.next; length += 1
            
        l = 0; r = length -1
        
        if len(val) == 0: return True
        
        while l < r:
            if val[l] != val[r]: return False
            l += 1; r -= 1
            
        else: return True
            