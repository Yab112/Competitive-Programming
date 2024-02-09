class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * len(nums)
        check_up = defaultdict(int)
        check_up[0] = 1
        counter = 0
        prefix_sum[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        for i in prefix_sum:
            counter += check_up[i % k]
            check_up[i%k] += 1
        return counter
            
        