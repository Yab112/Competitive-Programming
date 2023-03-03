class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x//2
        if x==0 or x==1:
            return x
        while low <= high:
            mid = low + (high - low)//2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                low = mid + 1
            
            elif mid ** 2 > x:
                high = mid -1
        
        return low-1
