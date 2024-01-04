class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_average = curr_sum / k
        j = 0
        for i in range(k,len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[j]
            j += 1
            max_average = max(max_average,curr_sum/k)
        return max_average