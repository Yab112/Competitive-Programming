class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        res = ""
        arr = [0] * (len(s) + 1)
        for i,j,k in shifts:
            if k == 1:
                arr[i] += 1
                arr[j + 1] -= 1
            else:
                arr[i] -= 1
                arr[j + 1] += 1
        pref_sum = list(accumulate(arr[:-1]))
        for i in range(len(s)):
            res += chr((ord(s[i])- 97 + pref_sum[i])%26 + 97)
        return res
       
        


        