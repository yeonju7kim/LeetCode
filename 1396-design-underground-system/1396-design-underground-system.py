class UndergroundSystem(object):                               
    def __init__(self):
        self.timeDuration = collections.defaultdict(lambda: collections.defaultdict(lambda: (0,0)))
        self.checkInPlace = collections.defaultdict(str)
        self.checkInTime = collections.defaultdict(int)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkInPlace[id] = stationName
        self.checkInTime[id] = t
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        accumulatedTime = self.timeDuration[self.checkInPlace[id]][stationName][0]
        peopleNum = self.timeDuration[self.checkInPlace[id]][stationName][1]
        self.timeDuration[self.checkInPlace[id]][stationName] = (t - self.checkInTime[id] + accumulatedTime, peopleNum + 1)
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        accumulatedTime = self.timeDuration[startStation][endStation][0]
        peopleNum = self.timeDuration[startStation][endStation][1]    
        return accumulatedTime / peopleNum
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)