from itertools import combinations
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max_perimeter,perimeter = 0, 0
        for i in range(len(nums)-2):
            a = nums[i]
            b = nums[i+1]
            c = nums[i + 2]
            if a + b > c and a + c > b and b + c > a:
                perimeter = a + b + c
                max_perimeter = max(max_perimeter, perimeter)

        return max_perimeter
            
            
            