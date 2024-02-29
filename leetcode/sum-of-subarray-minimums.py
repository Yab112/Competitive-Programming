from typing import List

class Solution:
    def __init__(self):
        self.right = []
        self.left = []

    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        self.right = [n] * n
        self.left = [-1] * n
        n_sm = self.n_smaler(arr)
        b_sm = self.b_smaller(arr)
        mod = 10**9 + 7
        return sum([(i - self.left[i]) * (self.right[i] - i) * val for i, val in enumerate(arr)]) % mod

    def b_smaller(self, nums2):
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[i] < nums2[stack[-1]]:
                stack.pop()
            if stack:
                self.right[i] = stack[-1]
            stack.append(i)
        return self.right

    def n_smaler(self, nums2):
        stack = []
        for i, value in enumerate(nums2):
            while stack and nums2[stack[-1]] >= value:
                stack.pop()
            if  stack:
                self.left[i] = stack[-1]
            stack.append(i)
        return self.left
