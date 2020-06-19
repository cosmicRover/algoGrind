'''
Time O(N) | Space O(1)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: return l1 or l2
        
        num1 = ""; num2 = ""
        
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
            
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
            
        num1 = str(int(num1) + int(num2))
        l1 = ListNode(-1)
        head = l1
        
        for x in num1:
            head.next = ListNode(int(x))
            head = head.next
            
            
        return l1.next