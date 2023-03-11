class Solution:
    def findMin(self, nums: List[int]) -> int:
        first,last=0,len(nums)-1
        if first==last or nums[first] < nums[last]:
            return nums[first]
        else:
            while first <= last:
                middle=first+(last-first)//2
                if nums[middle] < nums[middle-1] :
                    return nums[middle]
                elif nums[middle] > nums[last] :
                    first=middle+1
                else:
                    last=middle-1
            

