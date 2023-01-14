class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        first=0
        yab=len(nums)-1
        while first < yab:
            if nums[first]+nums[yab]==k:
                count+=1
                first+=1
                yab-=1
            elif nums[first]+nums[yab] < k:
                first+=1
            else:
                yab-=1
        return count
