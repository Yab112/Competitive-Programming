class Solution:
    def longestPalindrome(self, s: str) -> int:
      res = Counter(s)
      even = [i for i in res.values() if i % 2 == 0]
      odd =  [i for i in res.values() if i % 2 != 0]
      return sum(even) + sum(odd) - len(odd) + 1 if len(odd) != 0 else sum(even)