class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n_open =n_close = 0
        for i in s:
            if i == "(":
                n_open += 1
            elif i == ")" and n_open > 0:
                n_open -= 1
            else:
                n_close += 1
        return n_open + n_close
        