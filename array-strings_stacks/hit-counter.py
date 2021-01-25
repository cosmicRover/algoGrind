#queue approach

class HitCounter:

    def __init__(self):
        """
        key observations: 
            - timestamps always increase thus, no need for sorting
            - perfect place for a queue

        time O(n) total | space O(n)
        """
        self.hits = collections.deque()
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not timestamp: 
            return
        
        #sunce the timestamps are always increasing, we don't need to sort
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        #pop the hits from the left side
        while self.hits and timestamp-self.hits[0] >= 300: #if exceedimg last 5 minutes check
            self.hits.popleft()
            
        #length of leftover hits is the count of get hots
        return len(self.hits)

#array with indexing approach
