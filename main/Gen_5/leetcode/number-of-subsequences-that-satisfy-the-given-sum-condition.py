class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for ind,num in enumerate(nums):
            p = self.find_next_element(nums,num,target,ind)
            if  p != -1 :
                res += 2 ** (p - ind)
            else:
                return int(res) % (10**9 + 7)
        return int(res) % (10**9 + 7)
    def find_next_element(self,nums,i,target,ind):
        l, r = ind, len(nums) - 1
        while l <= r:
            mid = l + (r - l)//2
            temp =  nums[mid] + i
            if temp <= target:
                if mid + 1 == len(nums) or nums[mid + 1] + i > target:
                    return mid
                l = mid + 1
            
            else:
                r = mid - 1
        return -1
        

