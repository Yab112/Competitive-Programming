class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd_digits = {"1", "3", "5", "7", "9"}
        last_odd_index = -1

        for i, digit in enumerate(num):
            if digit in odd_digits:
                last_odd_index = i

        if last_odd_index == -1:
            return ""

        return num[:last_odd_index + 1]