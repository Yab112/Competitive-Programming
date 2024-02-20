class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        l = 0
        r = len(people) - 1
        people.sort()
        if len(people) == 1:return 1
        if people[0] == limit:return len(peole)

        while l  <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else :
                r -= 1
            boat += 1
        return boat
            
        
            

    
             
             
            
        
             

