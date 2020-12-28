class Item:
    def __init__(self, val):
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        item = Item(homepage)
        self.arr = [item]
        self.cp = 0
        
    def visit(self, url: str) -> None:
        #reattach from 0 to cp+1, so that forward history is erased
        self.arr = self.arr[:self.cp+1]
        item = item = Item(url)
        self.arr.append(item)
        self.cp += 1

    def back(self, steps: int) -> str:
        #two possible case handling on the negative direction
        if self.cp >= steps:
            self.cp -= steps
            
        elif self.cp < steps:
            self.cp = 0
            
        return self.arr[self.cp].val

    def forward(self, steps: int) -> str:
        #two possible case handling on the poritive direction
        if steps + self.cp <= len(self.arr) - 1:
            self.cp = steps + self.cp
            
        elif steps + self.cp > len(self.arr)-1:
            self.cp = len(self.arr)-1

        return self.arr[self.cp].val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)