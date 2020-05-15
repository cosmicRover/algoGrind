'''
sort lexographically using lambda function and priority [:]
the key observation in this problem is that letter logs have
words after the first word, and dig logs have a number after 
the first log. We use this to determine were to append a particular log

Time O(n + idSort + suffSort)
Space O(n for let + nums)
'''


class Solution:
    def reorderLogFiles(self, logs: [str]) -> [str]:
        if not logs:
            return []
        
        let = []
        dig = []
        
        #splice the words
        for x in logs:
            words = x.split()
            if words[1].isdigit():
                dig.append(x)
            else:
                let.append(x)
                
        print(let)
        print(dig)
        
        let.sort(key=lambda x: x.split()[0]) #sorts the identifiers first
        let.sort(key=lambda x: x.split()[1:]) #sorts the rest of the elements

        print(let)
        print(dig)
        
        return let + dig
        