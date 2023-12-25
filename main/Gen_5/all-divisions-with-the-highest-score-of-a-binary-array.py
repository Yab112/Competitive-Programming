class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        highest_score = {}
        n = len(nums)

        left_zeros = 0
        right_ones = nums.count(1)

        for i in range(n + 1):
            if nums[i - 1] == 0:
                left_zeros += 1
            else:
                right_ones -= 1

            score = left_zeros + right_ones

            if score not in highest_score:
                highest_score[score] = [i]
            else:
                highest_score[score].append(i)

        max_score = max(highest_score)
        max_indices = highest_score[max_score]

        return max_indices