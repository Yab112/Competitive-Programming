class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r =0,len(nums) - 1
        while l <= r:
            mid = l + ( r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if  r < 0:
            return 0
        elif nums[r] > target :
            return r
        else :
             return r + 1
        