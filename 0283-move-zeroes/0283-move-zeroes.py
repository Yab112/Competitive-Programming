class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left ,right = 0,1   # intializing two pointrs at the same point
        while right < len(nums) and left < right:
            if nums[left] == 0 and nums[right]!=0:
                nums[left] ,nums[right] = nums[right] ,nums[left]
                right += 1
                left += 1
            elif nums[left] != 0 and nums[right]==0:
                right += 1
                left += 1
            elif nums[right] != 0 and nums[left] != 0:
                right += 1
                left += 1
            else:
                right += 1
            
            
        
       
    """" check out this stack code, it ain't work for this scenario but it helped me to understand what is stack and how to work with stack,by the way when i say it ain't work i am teeling you that this isn't technically what they want you to do """
        # count = 0
        # stack = []
        # for i in nums:
        #     stack.append(i)
        #     print(stack)
        #     if i == 0:
        #         stack.pop()
        #         print(stack)
        #         count += 1
        # for i in range(count):
        #     stack.append(0)
        #     print(stack)
  
      
      
            
            
            
        
