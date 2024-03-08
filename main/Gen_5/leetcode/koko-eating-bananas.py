class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            mid = l + ( r - l) // 2
            if self.koko_check(piles,mid,h):
                r = mid - 1
            else:
                l = mid + 1
        return l 



    def koko_check(self,piles,mid,h):
        return h >= sum([ceil(i/mid) for i in piles])


       



        

        