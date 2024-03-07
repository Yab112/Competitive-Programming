class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            mid = l + (r - l)//2
            val = guess(mid)
            if val == 0:
                return mid
            elif val == -1:
                r = mid - 1
            else:
                l = mid + 1
