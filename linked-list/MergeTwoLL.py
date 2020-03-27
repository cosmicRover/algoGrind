# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Time O(m+n) where m and n are the length of the two lls
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Time O(m+n) where m and n are the length of the two lls
'''

class Solution:
    def mergeTwoLists(self, l1, l2):
        
        l = l1; r = l2
        dummy = cur = ListNode(-1)
        
        while l and r:
            if l.val > r.val:
                cur.next = r
                r = r.next
                
            else:
                cur.next = l
                l = l.next
                
            cur = cur.next
            
        cur.next = l or r
        
        return dummy.next