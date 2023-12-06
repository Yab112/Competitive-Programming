class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [0] * len(candies)
        for index,candie in enumerate(candies):
                temp = candie + extraCandies
                if all(temp >= i for i in candies):
                        result[index] = True
                else:
                        result[index] = False
        return result
        