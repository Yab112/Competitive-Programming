class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m
        for i in nums2:
            nums1[l] = i
            l += 1
        for i in nums1:
            for j in range(len(nums1)):
                try:
                    if nums1[j] > nums1[j + 1]:
                        nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
                except:
                    pass