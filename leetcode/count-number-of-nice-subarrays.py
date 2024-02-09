class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nice = 0
        pref = [0]*len(nums)
        dec = defaultdict(int)
        dec[0] = 1
        for i,value  in enumerate(nums):
            if value % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        pref[0] = nums[0]
        for i in range(1,len(nums)):
            pref[i] = pref[i - 1] + nums[i]
        for i in pref:
            if i - k in dec:
                nice += dec[i - k]
            dec[i] += 1
        return nice 
        
        
                
            
            