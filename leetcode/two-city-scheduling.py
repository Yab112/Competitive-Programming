class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        sorted_cost = sorted(costs,key=lambda x : x[0] - x[1])
        
        res = 0
        
        for i in range(len(costs)):
            if i < len(sorted_cost)//2:
                res += sorted_cost[i][0]
            else:
                
                res += sorted_cost[i][1]
        return res 
        