from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        max_sub = 0
        left = 0
        freq = Counter()
        
        for right in range(len(nums)):
            freq[nums[right]] += 1

            while len(freq) == k:
                max_sub += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
                
        return max_sub
