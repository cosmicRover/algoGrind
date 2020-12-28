"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        '''
        The trick here is to figure out a way to get the nodes in order.
        A recursive DFS fucntion call is used here. We use extra space to
        save the nodes so we can later re-attach into a DLL
        
        time O(n) | space O(n)
        
        '''
        if not head: return
        
        self.arr = []
        self.traverse(head)
        return self.composeLL(self.arr, head)
    
    def composeLL(self, arr, head):
        #setup a pointer to iterate, we get started with index 0
        temp = head
        temp = arr[0]
        
        #disconnect the pointers that are not needed
        temp.prev = None
        temp.child = None
        
        #attach the remaining
        for i in range(1, len(arr)):
            #get the current node and de-attach. prev/next will be re-written anyway
            #but make sure to remove child
            item = arr[i]
            item.child = None
            
            #reattach with the previous pointer
            temp.next = item
            item.prev = temp
            
            #increment the pointer
            temp = temp.next
            
        return head
            
        
    #recursively get child nodes first, then get next nodes
    def traverse(self, node):
        if node:
            #using extra space to save the nodes for later use
            self.arr.append(node)
            
            if node.child:
                self.traverse(node.child)
            
            if node.next:
                self.traverse(node.next)