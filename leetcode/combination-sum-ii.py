class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def back_track(idx,prev,prev_sum):
            if prev_sum > target :
                return 
            elif prev_sum == target:
                res.add(tuple(prev))
                return
            for j in range(idx,len(candidates)):
                if j > idx and candidates[j] == candidates[j - 1]:
                    continue
                prev.append(candidates[j])
                back_track(j + 1,prev,prev_sum + prev[-1])
                prev.pop()
        back_track(0,[],0)
        return res

        