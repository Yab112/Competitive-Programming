class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_array = []
        for half_number1 , half_number2 in zip(nums[:n],nums[n:]):
                new_array.append(half_number1)
                new_array.append(half_number2)
        return new_array
                
                
        