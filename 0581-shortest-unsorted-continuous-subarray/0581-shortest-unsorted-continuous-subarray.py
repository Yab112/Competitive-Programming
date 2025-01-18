class Solution:  
    def findUnsortedSubarray(self, nums: List[int]) -> int:  
        stack = []  
        l_bound, r_bound = float("inf"), float("-inf")  

        # Finding the left boundary  
        for ind, num in enumerate(nums):  
            while stack and num < nums[stack[-1]]:  
                l_bound = min(l_bound, stack.pop())  
            stack.append(ind)  

        # Reset the stack for the right boundary  
        stack = []  
        
        # Finding the right boundary  
        for ind in range(len(nums) - 1, -1, -1):  
            num = nums[ind]  
            while stack and num > nums[stack[-1]]:  
                r_bound = max(r_bound, stack.pop())  
            stack.append(ind)  
        print(l_bound,r_bound)
        # Calculate the length of the subarray  
        if r_bound - l_bound > 0:  
            return r_bound - l_bound + 1  
        return 0
        


    
