class NumArray:

    def __init__(self, nums: List[int]):
        self.NumArray = [0] + nums
        for i in range(1,len(self.NumArray)):
            self.NumArray[i] += self.NumArray[i-1]
        print(self.NumArray)
    def sumRange(self, left: int, right: int) -> int:
        return self.NumArray[right + 1] - self.NumArray[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)