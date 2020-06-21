# Splits in place a list in two halves, the first half is >= in size than the second.
# @return A tuple containing the heads of the two halves
class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):

        if not head or not head.next:
            return

        a, b = self._splitList(head)
        b = self._reverseList(b)
        head = self._mergeLists(a, b)
        
        
    def _splitList(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        middle = slow.next
        slow.next = None

        return head, middle

    # Reverses in place a list.
    # @return Returns the head of the new reversed list
    def _reverseList(self, head):

        last = None
        currentNode = head

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = last
            last = currentNode
            currentNode = nextNode #curr = curr.next

        return last

    # Merges in place two lists
    # @return The newly merged list.
    def _mergeLists(self, a, b):

        tail = a
        head = a

        a = a.next
        while b:
            tail.next = b
            tail = tail.next
            b = b.next
            if a:
                a, b = b, a
            
        return head