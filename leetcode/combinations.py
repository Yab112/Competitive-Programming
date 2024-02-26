class Solution:
    def __init__(self):
        self.arr = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i,path):
            if len(path) == k:
                self.arr.append(path[:])
                return 
            for choice in range(i + 1,n + 1):
                path.append(choice)
                backtrack(choice,path)
                path.pop()
        backtrack(0,[])
        return self.arr
            
        