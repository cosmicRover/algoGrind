# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        slow/fast pointer approach slow -> fast
        Find cycle, find cycle length, increment one pointer to length times,
        increment both pointers till they meet at the entrance
        
        time O(n) | space O(1)
        '''
        #find a cycle, if cycle find length
        slow = head
        fast = head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                #find the length of cycle
                length = self.findCycleLength(fast, slow)
                
                #find the cycle entrance
                return self.findCycleStart(length, head)
        return
    
    def findCycleStart(self, length, head):
        ptr1 = head
        ptr2 = head
        
        #move ptr1 length times
        for i in range(length):
            ptr1 = ptr1.next
            
        #keep moving both pointers till they meet
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return ptr2
    
    def findCycleLength(self, fast, slow):
        length = 0
        while True:
            slow = slow.next
            length += 1
            
            if fast == slow: break
            
        return length
    
    
#     def detectCycle(self, head: ListNode) -> ListNode:
#         '''
#         hash table approach, uses O(n) extra space and O(n) time
#         '''
#         dic = {}
        
#         while head:
#             if head in dic:
#                 return head
#             dic[head] = 1
#             head = head.next
#         return head