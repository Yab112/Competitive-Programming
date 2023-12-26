class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_index = 0 
        pre_alligned = 0

        for i, flip in enumerate(flips):
            max_index = max(max_index, flip)
            
            if max_index == i + 1:
                pre_alligned += 1

        return pre_alligned