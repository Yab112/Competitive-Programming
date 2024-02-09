class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_sum = defaultdict(int, {0: 0})
        res = 0   
        cursum = 0
        for i in nums:
            cursum += i
            if cursum == k:
                res += 1
            if cursum - k in prev_sum :
                res += prev_sum[cursum - k]
   
            prev_sum[cursum] += 1
        return res