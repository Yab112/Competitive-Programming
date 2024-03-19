class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pref, cur_sum, res = [0] * len(s), 0, []
        candles_pos = [i for i, symbol in enumerate(s) if symbol != "*"]
        for i in range(len(s)):
            if s[i] == "*":
                cur_sum += 1
            pref[i] = cur_sum
        
        for q in queries:
            l = self.min_max_el(candles_pos,q[0])
            r = self.min_max_el(candles_pos,q[1] + 1) - 1 
            print(l,r)
            res.append(pref[candles_pos[r]] - pref[candles_pos[l]] if l < r else 0)
        return res
    
    def min_max_el(self,nums,x):
        l, r,= 0,len(nums) - 1
        while l <= r:
            mid = l + ( r- l)//2
            if nums[mid] < x:
                l = mid + 1
            else:
                r = mid - 1

        return l