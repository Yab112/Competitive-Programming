class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       array = self.remove_duplicates(nums)
       len_array = len(array)
       print(len_array,'nums = ' ,array)
       return 
    def remove_duplicates(self,array)->list:
        l = 0
        r = 1
        while l < r and r < len(array):
            if array[l] != array[r]:
                r += 1
                l += 1
            else:
                array.remove(array[l])
        return array