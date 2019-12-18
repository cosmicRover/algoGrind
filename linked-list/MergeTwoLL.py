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
        #init our new linked list
        newLL = pointer = ListNode(-1)
        
        #going through iteratively as long as l1 or l2 is not null
        while l1 and l2:
            # comapre and get the smaller value
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
            else:       #l2.val < l1.val or if they are equal
                pointer.next = l2
                l2 = l2.next
            
            pointer = pointer.next #always increment pointer to the newLL to next
            
        pointer.next = l1 or l2 # reattach the leftovers from l1 or l2
        
        return newLL.next