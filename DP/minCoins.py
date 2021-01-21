class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp problem approach. find small problem -> init dp table
        
        for this problem, the smaller problem is to reach a sum < the given amount.
        Since there are only one set of resources (coins) and one target, single
        rowed dp table can be used.
        
        '''
        
        #init dp table with +inf since we need min. our base line is always 0 
        #thus we add one more cell than amount
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        
        #calcualte minimum for each given coin
        for coin in coins:
            
            #only start from coin index since sum < coin can't be reached anyway
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i], dp[i-coin]+1)
                
        return dp[-1] if dp[-1] != float("inf") else -1
        
        
        '''
        small problem discussion:
        
        let's say I want to to reach 8 with coin 2, how many coins will I end up using?
        I will need 2+2+2+2 coins. Ineed to reach the exact amount. Is there a formula for this?
        
        I reach 0 with 0 coins set manually as starting point
        I reach 1 with inf coins aka the default
        I reach 2 with 1 coin 
        I reach 3 with 2 coins
        I reach 4 with 2 coins
        
        formula: min(current-dp-val, previously-computed-value-from-dp + 1)
        reaching 2: min(+inf, dp[2-2]+1) => 1
        reaching 3: min(+inf, dp[3-2]+1 => inf+1) => inf
        reaching 4: min(+inf, dp[4-2]+1 => 2) => 2
        '''
        
        