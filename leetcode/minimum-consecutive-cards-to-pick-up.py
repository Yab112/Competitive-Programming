class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
       temp = {}
       minim = len(cards)
       flag = False
       for i,value  in enumerate(cards):
            if value not in temp:
                temp[value] = i
            elif value in temp:
                flag = True
                minim = min(minim,i - temp[value] + 1)
                temp[value] = i
       return minim if flag else -1

