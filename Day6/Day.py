class Day:
    def __init__(self, timeList ):
        self.time0 = timeList[0]
        self.time1 = timeList[1]
        self.time2 = timeList[2]
        self.time3 = timeList[3]
        self.time4 = timeList[4]
        self.time5 = timeList[5]
        self.time6 = timeList[6]
        self.time7 = timeList[7]
        self.time8 = timeList[8]

    def newDay(self):
        newDay = Day([self.time1, self.time2, self.time3, self.time4, self.time5, self.time6, (self.time7 + self.time0), self.time8, self.time0])
        return newDay

    def getTotal(self):
        return sum([self.time0, self.time1, self.time2, self.time3, self.time4, self.time5, self.time6, self.time7, self.time8])