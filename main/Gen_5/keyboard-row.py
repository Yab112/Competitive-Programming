class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop" 
        second_row = "asdfghjkl" 
        third_row = "zxcvbnm"
        out_put = []
        for i in words:
            if all(char.lower() in first_row for char in i ):
                out_put.append(i)
            if all(char.lower() in second_row for char in i ):
                out_put.append(i)
            if all(char.lower() in third_row for char in i ):
                out_put.append(i)
        return out_put 

        