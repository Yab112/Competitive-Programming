class Solution:

    def __init__(self, nums: List[int]):
        self.dict = defaultdict(list)
        for index,num in enumerate(nums):
            self.dict[num].append(index)
        print(self.dict)
    def pick(self, target: int) -> int:
        if self.dict[target] and len(self.dict[target]) > 0:
            indices = self.dict[target]
            randomInx = random.choice(indices)
            return randomInx


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)