class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collector = []
        my_dict = {key:value for value,key in enumerate(nums)}
        for i in nums:
            if target - i in my_dict:
                if nums.index(i) != my_dict[target-i]:
                        return [nums.index(i),my_dict[target-i]]