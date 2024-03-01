class Solution:
    def __init__(self):
        self.arr = []
        self.path = []
    def subsets(self, nums: List[int]) -> List[List[int]]:


        def sub_set(start):
            self.arr.append(self.path[:])
            for j in range(start,len(nums)):
                if nums[j] not in self.path:
                    self.path.append(nums[j])
                    sub_set(j + 1)
                    self.path.pop()
        sub_set(0)
        return self.arr
        