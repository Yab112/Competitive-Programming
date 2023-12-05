class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        walk = 0
        remaining_capacity = capacity 
        for i,j in enumerate(plants):
            
            if remaining_capacity >= j:
                
                 remaining_capacity  -= j
                
                 walk += 1
            else:
                walk += 2*i 
                walk += 1
                remaining_capacity = capacity - j
        return walk 
    
                
                
            