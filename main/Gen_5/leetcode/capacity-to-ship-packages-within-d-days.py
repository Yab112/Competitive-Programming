class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = l + ( r - l)//2
            if self.simulate_sum(weights,mid) > days:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def simulate_sum(self,w,mid_w):
        l = res = day = 0
        for i in w:
            if i + res <= mid_w:
                res  += i
            else:
                day += 1
                res = i 
        return day + 1
            



