class Solution:
    def __init__(self):
        self.visited = set()

    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        for i in range(len(nums)):
            if i  in self.visited:
                continue
            
            slow, fast = i, self.__privateHelper(i, nums)
            while True:
                if nums[slow] * nums[fast] > 0 and nums[self.__privateHelper(fast, nums)] * nums[fast] > 0:
                    slow, fast = self.__privateHelper(slow, nums), self.__privateHelper(self.__privateHelper(fast, nums), nums)
                    self.visited.add(slow)
                    if fast == slow :
                        if fast != self.__privateHelper(fast, nums):
                            return True
                        break
                else:
                    break

        return False

    def __privateHelper(self, index, nums):
        return (index + nums[index]) % len(nums)
