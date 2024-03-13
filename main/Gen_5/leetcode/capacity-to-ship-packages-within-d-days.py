class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_w = max(weights)
        max_w = sum(weights)
        while min_w < max_w:
            mid_w = min_w + (max_w - min_w) // 2
            if self.predict(weights, mid_w, days):
                max_w = mid_w
            else:
                min_w = mid_w + 1
        return min_w
    
    def predict(self, weights, mid_w, days):
        l = r = 0
        res = 0
        day = 1
        while r < len(weights):
            if res + weights[r] <= mid_w:
                res += weights[r]
            else:
                day += 1
                res = weights[r]
            r += 1
        return day <= days
