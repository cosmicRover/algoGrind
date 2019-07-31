

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        #init fast and slow to head
        slowPointer = fastPointer = head
        
        # while slow, fast and fast.next is not None
        while slowPointer and fastPointer and fastPointer.next:
            # advance slowPointer by one and fastPointer by two
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            
            if slowPointer == fastPointer:
                return True
        return False
        
        
        