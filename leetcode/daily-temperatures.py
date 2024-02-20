class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        dic = {}
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                temp = stack.pop()
                dic[temp] = i
            stack.append(i)
        while stack:
            temp = stack.pop()
            dic[temp] = "None"
        for i in range(len(temperatures)):
            if dic[i] != "None" :
                stack.append(dic[i] - i)
            else:
                stack.append(0)
        return stack



        
        