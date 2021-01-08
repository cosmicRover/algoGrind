# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
            
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None

        while st1 or st2 or carry:
            
            #a way to sum two numbers left to right
            #get the digits from their respective stacks
            d1 = st1.pop() if st1 else 0
            d2 = st2.pop() if st2 else 0
            
            #addition: num1 + num2 + carry, base
            carry, digit = divmod(d1 + d2 + carry, 10)
            
            #reversing values generated from divmod in place
            #make a new_node, slide old one to next position
            #make new_node the head
            
            head_new = ListNode(digit)
            head_new.next = head
            head = head_new
              
        return head