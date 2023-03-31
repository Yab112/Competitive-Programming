class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if it wasn't in_place 
            # stack = []
            # for i in range(len(nums)-(k),len(nums)):
            #     stack.append(nums[i])
            # for j in range(0,len(nums)-(k)):
            #     stack.append(nums[j])
        # in_place
        n = len(nums)
        k = k % n                 
        nums[n - k:] = nums[n - k:][::-1]  
        nums[:n - k] = nums[:n - k][::-1] 
        nums[:] = nums[::-1] 
        
            
        
        
