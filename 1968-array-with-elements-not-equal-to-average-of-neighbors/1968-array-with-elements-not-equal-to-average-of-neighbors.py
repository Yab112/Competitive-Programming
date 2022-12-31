class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        yab=len(nums)
        for i in range(0,yab-1):
            num1,num2,num3=nums[i-1],nums[i],nums[i+1]
            if num1 < num2 < num3 or num1 > num2> num3:
                nums[i],nums[i+1]=nums[i+1],nums[i]
            
        return nums
        