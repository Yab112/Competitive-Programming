class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = "0"
        for i in range(len(num)):
                if i+1 < len(num) and i + 2 < len(num) and num[i] == num[i+1] == num[i+2]:
                        if int(largest) <= int(num[i:i+3]):
                                largest = num[i:i+3]
        return largest if "0" != largest else ""