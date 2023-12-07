class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(0,len(nums),2):
                if i + 1 < len(nums):
                        new_list += [nums[i+1]] * nums[i]
                        
                        
        return new_list
                        
        