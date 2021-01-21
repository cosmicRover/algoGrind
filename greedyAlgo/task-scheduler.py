class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        '''
        use greedy appraoch. max first -> min last
        
        One thing to realzie is that there can be a maxinmum of
        (most frequent char - 1) * n idel time
        
        ["A","A","A","B","B","B"] n = 2
        A = 3
        
        idle = (3-1) * 2 = 4 possible idle time
        [A][idle][idle][A][idle][idle][A]
        
        fill-in/add other tasks
        [A][B][idle][A][B][idle][A][B]
        
        thus, left over idle time 2 + len(tasks) = 8 the minimum time required to complete all tasks
        
        time O(# of total tasks that need to be processed)
        space O(1) since length of 26 is considered O(1)
        
        '''
        
        #since the tasks are only capital letter of the alphabets, 
        #I can use array of length 26 to keep track of their frequencies
        frequencies = [0]*26
        
        #populate the arr with tasks
        for t in tasks:
            index = ord(t)-ord("A") #find a given letter's index and increment it
            frequencies[index] += 1
            
        #sort so that we can pop max first
        frequencies.sort()
        
        #pop max and calcualte max possible cool-time
        _max = frequencies.pop()
        coolTime = (_max - 1)*n
        
        #loop through and subtract coolTime
        #this will yield the minimum number of coolTime needed to do our work
        while frequencies and coolTime > 0:
            item = frequencies.pop()
            coolTime -= min(_max-1, item)
            
        #reset coolTime to 0 if it is below 0
        coolTime = max(0, coolTime)
        
        #coolTime + len(tasks) is the minimum time we need to complete task
        return coolTime + len(tasks)