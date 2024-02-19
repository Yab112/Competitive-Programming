class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        stack.append(nums2[0])
        dic = {}
        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                temp = stack.pop()
                dic[temp] = nums2[i]
            stack.append(nums2[i])
        while stack:
            temp = stack.pop()
            dic[temp] = -1
        for i in nums1:
            stack.append(dic[i])
        return stack
            

           
