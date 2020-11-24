class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        #save the levels we traverse, init with -1
        levels = {-1:0}
        maxLength = 0
        
        input = input.split("\n")

        for item in input:
            #get the tab counts, as they are depths
            depth = item.count("\t")
            
            #save the depth as the previous depth + length - depth(\t count)
            #on first iteration 0, -1 gets pulled and added, thus we have -1:0 to init
            levels[depth] = levels[depth-1] + len(item) - depth
            
            #if we encounter a file denoted with ".", we save maxLength
            if "." in item:
                maxLength = max(maxLength, levels[depth] + depth) #add in \t count here
            
        return maxLength