class Solution:  
    def minCostClimbingStairs(self, cost: List[int]) -> int:  
        n = len(cost)  
        if n == 0: return 0    
        if n == 1: return cost[0]  

        first = 0   
        second = 0 

        for i in range(n - 1, -1, -1):  
            current = cost[i] + min(first, second)  
            first, second = second, current  

        return min(first, second) 