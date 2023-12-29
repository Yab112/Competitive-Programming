class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dictionary = {}
        sorted_nums = sorted(nums)
        for i,j in enumerate(sorted_nums):
            if j not in dictionary:
                dictionary[j] = i
        return [dictionary[i] for i in nums]
   
        
    
        
                
            