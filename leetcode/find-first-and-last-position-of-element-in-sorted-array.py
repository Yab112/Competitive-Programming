class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l , r = 0,len(nums) - 1
        while l <= r:
            mid = l + ( r - l) // 2
            if nums[l] == target and nums[r] == target:
                    return [l,r]
            elif nums[mid] == target:
                mid_l = mid - 1
                mid_r = mid + 1
                while (mid_l >=0 and mid_r < len(nums)) and (nums[mid_l]  == target or nums[mid_r]  == target):
                    if nums[mid_l]  == target:
                        mid_l -= 1
                    if nums[mid_r]  == target:
                        mid_r += 1
                return [mid_l + 1,mid_r -1]
            elif nums[mid] > target :
                r = mid - 1
            else:
                l = mid + 1
        return [-1,-1]