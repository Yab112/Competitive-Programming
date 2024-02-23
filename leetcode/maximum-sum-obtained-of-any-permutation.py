class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        frequency = [0]*(len(nums) + 1)
        for i in requests:
            frequency[i[0]] += 1  
            if  i[1] + 1 < len(nums) :
                frequency[i[1] + 1] -= 1
        fre_pref = list(accumulate(frequency))
        new_pref = sorted(fre_pref[:-1]) +[fre_pref[-1]]
        nums.sort()
        return (sum([ new_pref[i] * nums[i] for i in  range(len(nums))])) % ((10 ** 9) + 7)