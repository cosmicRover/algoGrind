class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        '''
        bfs approach. pop(0)
        ppid is the parent node and pid is the child node.
        
        time O(n) | space O(n)
        
        '''
        
        if not pid or not ppid: return 
        
        graph = collections.defaultdict(list)
        
        for u, v in zip(ppid, pid):
            graph[u].append(v)
            
        #bfs starting on process that needs to be killed
        killed = []
        q = [kill]
        
        while q:
            item = q.pop(0)
            killed.append(item)
            
            for node in graph[item]:
                q.append(node)
                
        return killed