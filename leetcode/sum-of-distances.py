class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        fre_hash =  {}
        pref_hash = {}
        res = [0] * len(nums)
        for i,num in enumerate(nums):
            if num not in fre_hash:
                fre_hash[num] = 1
                pref_hash[num] = i
            else:
                res[i] = i * fre_hash[num] - pref_hash[num]
                pref_hash[num] += i
                fre_hash[num] += 1
        pref_hash.clear()
        fre_hash.clear()
         
        for i in range(len(nums)-1,-1,-1):
            if nums[i] not in fre_hash:
                fre_hash[nums[i]] = 1
                pref_hash[nums[i]] = i
            else:
                res[i] += pref_hash[nums[i]] - (i * fre_hash[nums[i]])
                pref_hash[nums[i]] += i
                fre_hash[nums[i]] += 1
        return res

