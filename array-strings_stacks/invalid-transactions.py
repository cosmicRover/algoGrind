import collections

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        '''
        this isn't a tricky question but there are certainly ambiguity
        
        invalid if:
        -the amount exceeds $1000, or;
        -if it occurs within (and including) 60 minutes of another 
        transaction with the same name in a different city. In this case both
        current and previous transactions are invalid
        
        what it doesn't mention is that we not only look at the last transaction,
        we look at ALL transactions that occours under a specific name hence an 
        iterable dict (collections.defaultdict(list)) so we also always append updated
        transaction
        
        time O(n^2) | space O(n) for defaultdict

        '''
        
        if not transactions: return []
        
        #iterble hash table to remember transactions
        actions = collections.defaultdict(list)
        
        invalids = set()
        
        for transaction in transactions:
            name, time, price, location = transaction.split(",")
            
            #check price
            if int(price) >= 1000:
                invalids.add(transaction)
                
            #if other transaction exists with the same name, iterate over them
            if name in actions:
                for item in actions[name]:
                    prevTime, prevPrice, prevLocation = item.split(",")
                    
                    #if a transaction was done with 50 minutes in different city, it's invalid
                    if abs(int(prevTime)-int(time)) <= 60 and prevLocation != location:
                        invalids.add(name+","+item)
                        invalids.add(transaction)
                    
                    
            #always save the transactions. This is an iterable dict, so we append
            actions[name].append(time+","+price+","+location)
            
        return invalids
                