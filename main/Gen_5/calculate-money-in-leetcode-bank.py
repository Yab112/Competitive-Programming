class Solution:
    def totalMoney(self, n: int) -> int:
        result = 0
        week = 0
        while n - 7 >= 0:
            result += sum(range(week + 1,week + 1 + 7))
            week += 1
            n -= 7
        result += sum(range(week + 1,n + week + 1))
        return result