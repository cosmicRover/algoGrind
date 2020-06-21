class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #why not just remember the nodes. keep life simple
        map = {None : None}
        
        temp = head
        
        while temp:
            map[temp] = Node(temp.val,temp.next,temp.random)
            temp = temp.next
        
        temp = head
        
        while temp:
            map[temp].next = map[temp.next]
            map[temp].random = map[temp.random]
            temp = temp.next
        
        return map[head]