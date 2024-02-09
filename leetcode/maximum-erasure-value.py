class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        temp = defaultdict(int)
        summ=0
        count=0
        for i in range(len(nums)):
            summ+=nums[i]
            temp[nums[i]]+=1
            while temp[nums[i]] >1:
                summ-=nums[l]
                temp[nums[l]]-=1
                l+=1
            count=max(summ,count)
            
        return count
            