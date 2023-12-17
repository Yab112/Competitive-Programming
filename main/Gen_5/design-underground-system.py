class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.check_out = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_in[id]
        journey_key = (start_station, stationName)
        if journey_key not in self.check_out:
            self.check_out[journey_key] = (t - check_in_time, 1)
        else:
            total_time, count = self.check_out[journey_key]
            self.check_out[journey_key] = (total_time + t - check_in_time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        journey_key = (startStation, endStation)
        total_time, count = self.check_out[journey_key]
        return total_time / count




# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)