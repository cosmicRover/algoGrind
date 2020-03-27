# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Time O(m+n) where m and n are the lengths of the two LinkedLists
Space O(m+n) on the recursive callstack
'''
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return 
        if len(lists) == 1:
            return lists[0]

        mid = len(lists)//2

        #keeps dividing till there is only single ones
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])

        #start merging lists recurisvely
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = cur = ListNode(-1)

        #position l or r based on their values
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next

        #if there is an l or r left, cur.next will be pointed there
        cur.next = l or r

        #returns dummy.next as the real lists
        return dummy.next