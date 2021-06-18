class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        UMPIRE
        
        Understand:
        test cases: 1-2-3-4-5, k = 2 => 1-2-3-5
                    
                    1, n= 1 => []
                    
                    1-2 n = 1 => 1
                    
        Match:
        linkedlist find k'th node from both sides approach
        
        Plan:
        use ll find k'th node from both sides algorithm, with modification
        
        Implement:
        '''
        #init curr, first, second, length pointers
        curr = head
        second = None
        length = 0
        prev = None

        #loop through the list with curr
        while curr:
            length += 1

            #if second is available, increment second
            #also save prev as second
            if second:
                prev = second
                second = second.next

            #if length == k, save this as first and init second as head
            if length == n:
                second = head

            curr = curr.next

        #edge case, remove first node if prev is None
        if not prev:
            return head.next

        #remove prev's next node
        prev.next = prev.next.next

        return head

        '''
        Review:
        Use the test cases/run to confirm the code
        
        Evaluate:
        time O(n) | space o(1)
        '''
