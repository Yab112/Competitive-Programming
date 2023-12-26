class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights) - 1):
            for j in range(len(heights) - i -1):
                if j + 1 < len(heights) and  heights[j] < heights[j + 1]:
                    temp1 = heights[j]
                    temp2 = names[j]
                    heights[j] = heights[j + 1]
                    names[j] = names[j + 1]
                    heights[j + 1] = temp1
                    names[j + 1] = temp2
        return names