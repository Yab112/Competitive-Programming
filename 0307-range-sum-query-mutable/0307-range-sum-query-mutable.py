class BinaryIndexedTree:  
    def __init__(self, size):  
        self.size = size  
        self.tree_array = [0] * (self.size + 1)    

    @staticmethod  
    def lsb(index):  
        return index & -index  

    def update(self, index, delta):  
        while index <= self.size:  
            self.tree_array[index] += delta  
            index += self.lsb(index)  

    def sum(self, index):  
        total = 0  
        while index > 0:  
            total += self.tree_array[index]  
            index -= self.lsb(index)  
        return total  

    def range_sum(self, left, right):  
        return self.sum(right) - self.sum(left - 1)  


class NumArray:  
    def __init__(self, nums):  
        self.size = len(nums)  
        self.bit = BinaryIndexedTree(self.size)  
        self.nums = [0] * self.size  
        
        for i in range(self.size):  
            self.update(i, nums[i])  

    def update(self, index, val):  
        delta = val - self.nums[index]  
        self.nums[index] = val  
        self.bit.update(index + 1, delta)  

    def sumRange(self, left, right):  
        return self.bit.range_sum(left + 1, right + 1)   


# Example usage:  
# nums = [1, 3, 5]  
# obj = NumArray(nums)  
# print(obj.sumRange(0, 2))  # Output: 9  
# obj.update(1, 2)            # nums = [1, 2, 5]  
# print(obj.sumRange(0, 2))  # Output: 8  
