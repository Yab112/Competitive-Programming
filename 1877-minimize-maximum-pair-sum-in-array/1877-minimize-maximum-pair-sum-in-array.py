class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        first=0
        last=len(nums)-1
        maxx=[]
        while first < last:
            yab=nums[first]+nums[last] 
            # if last - first >=1:
            maxx.append(yab)
            last-=1
            # else :
            first+=1
        return max(maxx)