class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backTrack(path):
            if len(path) == len(nums):
                self.res.append(path[:])
            for i in nums:
                if i not in path:
                    path.append(i)
                    backTrack(path)
                    path.pop()
        backTrack([])
        return self.res

