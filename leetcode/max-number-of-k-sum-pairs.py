class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        r = 0
        operation = 0
        dec = collections.Counter(nums)
        for num in nums:
            temp = k - num
            if dec[temp] > 0 and dec[num] > 0:
                if temp == num and dec[num] == 1:
                    continue
                else:
                    operation  += 1
                    dec[temp]-=1
                    dec[num]-=1
        return operation
                    
                
            
        