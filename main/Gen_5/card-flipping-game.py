class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        minimum = float('inf')
        same_cards = set()
        
        # Find the cards with the same number on both front and back
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                same_cards.add(fronts[i])
        
        # Check each card to determine the minimum valid number
        for i in range(len(fronts)):
            if fronts[i] not in same_cards:
                minimum = min(minimum, fronts[i])
            if backs[i] not in same_cards:
                minimum = min(minimum, backs[i])
         
        return minimum if minimum != float('inf') else 0