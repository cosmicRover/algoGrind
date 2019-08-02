# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# O (n) time | O(n/2) space
class Solution(object):
    def isPalindrome(self, head):

        if not head or not head.next:
            return True

        # 1. Get the midpoint (slow)
        slow = fast = cur = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
    
        # 2. Push the second half into the stack
        stack = [slow.val]
        while slow.next:
            slow = slow.next
            stack.append(slow.val)

        # 3. Comparison
        while stack:
            if stack.pop() != cur.val:
                return False
            cur = cur.next
    
        return True