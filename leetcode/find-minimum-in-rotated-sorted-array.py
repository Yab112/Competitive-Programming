class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r ,res = 0,len(nums) - 1,float("inf")
        if len(nums) == 1:
            return nums[0]
        while l <  r:
            mid = l + (r - l )// 2
            
            if nums[r] > nums[mid]:
                r = mid 

            elif nums[r] < nums[mid]:
                l = mid + 1
        return nums[l]
           

