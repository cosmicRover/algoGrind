# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        slow/fast pointer approact. slow.next -> fast.next.next
        using extra memory is trivial
        for constant memory, need to reverse second half of LL
        
        time O(n) | space O(1)
        '''
        #get to the middle of LL
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
          
        #save a copy for later use
        copy_slow = slow
        
        #reverse the second half of the LL and get the pointer
        right_head = self.reverseLL(slow)
        
        #now compare the left half with the right half
        ptr = head
        while ptr and right_head:
            #the reason we don't just break because if LL has an odd
            #length, numbers won't match but still be a palindrome
            if ptr.val != right_head.val:
                break
            
            ptr = ptr.next
            right_head = right_head.next
            
        #revert back the right half if we cant modify it
        self.reverseLL(copy_slow)
        
        #if either one has been fully traversed, we have valid palindrome
        if not ptr or not right_head:
            return True
        
        return False
         
    def reverseLL(self, head):
        #reverse LL by inserting prev in between, then making prev head
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev