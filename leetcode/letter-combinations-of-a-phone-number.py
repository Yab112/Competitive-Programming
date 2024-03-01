class Solution:
    def __init__(self):
        self.res  = []
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        if not digits:
            return []
        def back_track(i,path):

            if len(path) == len(digits):
                self.res.append("".join(path))
                return
            d = dic[int(digits[i])]
            for j in range(len(d)):

                path.append(d[j])
                back_track(i + 1,path)
                path.pop()
        back_track(0,[])
        return self.res