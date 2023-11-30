class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        min_length = min(len(s) for s in strs)
        longest = ""

        for i in range(min_length):
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                longest += char
            else:
                break

        return longest
