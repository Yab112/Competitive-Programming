import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        return int(math.log(n, 4)) - math.log(n, 4)  == 0.0
        