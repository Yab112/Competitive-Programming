class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        no_less = [ i for i in nums if i < pivot]
        no_greater = [ i for i in nums if i > pivot]
        pivot_no = [i for i in nums if i == pivot]
        return no_less + pivot_no + no_greater
        