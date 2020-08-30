'''
The trick is to use existing DS to save events as they come in
Time O(1)????? | Space O(num of chekin + (time/count)^2)
'''

class UndergroundSystem:

    def __init__(self):
        self.checkin={}
        self.count={}
        self.time={} 
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkin:
            return
        
        item = self.checkin[id]
        del self.checkin[id] #deleting from checkin
        
        key = item[0]+stationName # key = start+end station
        
        if key not in self.time:
            self.time[key] = 0
            
        self.time[key] += (t-item[1])
        
        #saving how many times start to end occours
        if key not in self.count:
            self.count[key] = 1
        else:
            self.count[key]+= 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation+endStation
        if key not in self.time:
            return
        
        num = self.time[key]
        return num/self.count[key] #get time, then num of occurnace, then return average
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)