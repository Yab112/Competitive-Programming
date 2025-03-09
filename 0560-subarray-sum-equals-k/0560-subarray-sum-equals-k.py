class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        countStore = defaultdict(int)
        countStore[0] = 1
        prefSum = count = 0
        for num in nums:
            prefSum += num
            if prefSum - k in countStore:
                count += countStore[prefSum - k]
            countStore[prefSum] += 1
        return count
        
                
