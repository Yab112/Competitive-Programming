class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start,path,path_sum):
            if path_sum > target:
                return
            if path_sum == target:
                res.append(path[:])
                return 
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path,path_sum + candidates[i])
                path.pop()
        backtrack(0,[],0)
        return res

           