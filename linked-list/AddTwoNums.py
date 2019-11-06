# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SLL:
    
    def __init__(self):
        self.head = None
    
    def setHead(self, val):
        self.head = ListNode(val)
    
    def addANode(self, val):
        current = self.head
        
        if current is None:
            self.setHead(val)
            return
        
        while current.next:
            current = current.next
        current.next = ListNode(val)
            

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = ""
        num2 = ""
        
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        #reversing the vars
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        #adding the strings by converting them into nums first
        num1 = int(num1) + int(num2)
        num1 = str(num1)
        num1 = num1[::-1]
        
        #init a new Singly Linked List and retrun the head as the output
        newLL = SLL()
        
        for x in num1:
            newLL.addANode(x)
            
        return newLL.head
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
     