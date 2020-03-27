import collections

class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        #init DS for graph BFS operations
        dead_set = set(deadends)
        queue = collections.deque([('0000', 0)]) #using built in pq from python
        visited = set('0000')

        while queue:
            (string, steps) = queue.popleft()
            
            if string == target:
                return steps
            
            elif string in dead_set:
                continue
            
            #generate new combinations and check if they are blocked
            #if not blocked, append them to the queue for further traversal
            for i in range(4):
                digit = int(string[i])
                
                #since we can only move forward and backwards, there is 
                #only two moves
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_string = string[:i]+str(new_digit)+string[i+1:]
                    
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, steps+1))
        return -1