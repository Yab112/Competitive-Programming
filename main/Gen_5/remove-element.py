class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Number of occurrences of val
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
                k += 1

        l = 0  # 
        r = len(nums) - 1  

        while l <= r:
            while l <= r and nums[l] != "_":
                l += 1

            while l <= r and nums[r] == "_":
                r -= 1

            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        return len(nums) - k