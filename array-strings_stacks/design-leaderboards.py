import heapq

class Leaderboard:
    '''
    Used a dictionary. Using a heapq to store all the high scores might be smarter
    but replacing and reseting 
    
    time O(n log n) for sorting | Space O(n)
    '''

    def __init__(self):
        self.players = {}
        
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.players:
            self.players[playerId] = score
        else:
            self.players[playerId] += score

    def top(self, K: int) -> int:
        # heapq.nlargest(K, self.players.values()) O(n log k) time
        top = sorted(self.players.values()) # O(n log n) time
        return sum(top[-K:])
        

    def reset(self, playerId: int) -> None:
        self.players[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)