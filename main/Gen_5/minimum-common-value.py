class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        min_member = float("inf")
        l1=l2 = 0
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] == nums2[l2]:
                if min_member > nums1[l1]:
                    min_member = nums1[l1]
                l1 += 1
                l2 += 1
            elif nums1[l1] > nums2[l2]:
                l2 += 1
            else:
                l1 += 1
            
        return min_member if min_member != float("inf") else -1
        