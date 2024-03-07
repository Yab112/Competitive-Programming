# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        print(2**31 - 1)
        while l <= r:
            mid = l + ( r- l) //2
            if  isBadVersion(mid) == True and isBadVersion(mid - 1) == False:
                return mid
            elif isBadVersion(mid) == True and isBadVersion(mid - 1) == True:
                r = mid - 1
            else:
                l = mid + 1 
