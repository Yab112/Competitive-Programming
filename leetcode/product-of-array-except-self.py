class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array1 = [0] * len(nums)
        array2 = [0] * len(nums)
        array3 = [0] * len(nums)
        array1[0] = 1
        array2[len(nums)-1] = 1

        for i in range(1,len(nums)):
            array1[i] = array1[i-1] * nums[i-1]
        print(array1)
        for i in range(-2,-len(nums)-1,-1):
            array2[i] = array2[i+1] * nums[i+1]
        print(array2)
        
        for i in range(len(array1)):
            array3[i] = array1[i] * array2[i]
         

        return array3
        