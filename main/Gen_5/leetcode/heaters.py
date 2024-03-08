class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0
        for house in houses:
            radius  = max(radius,self.nearest_heater(heaters,house))
        return radius 

    def nearest_heater(self,heaters,house):
        l = 0 
        r = len(heaters) - 1
        min_dist = float("inf")
        while l <= r:
            mid = l + ( r - l )//2
            min_dist = min(min_dist,abs(heaters[mid] - house))
            if heaters[mid] > house:
                r = mid - 1
            else:
                l = mid + 1
        return min_dist





