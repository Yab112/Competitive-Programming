from collections import Counter

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        unique_elements = sorted(list(set(nums)), reverse=True)
        operation = 0
        reduction_ops = 0

        for element in unique_elements:
            count = counts[element]
            operation += reduction_ops
            reduction_ops += count

        return operation