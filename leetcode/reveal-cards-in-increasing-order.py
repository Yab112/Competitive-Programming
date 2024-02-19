class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        temp = sorted(deck)
        my_deque = deque(sorted(deck))
        r_1 = self.t(my_deque)
        j = 0
        num  =[0]*len(temp)
        for i in r_1:
            num[temp.index(i)] = temp[j]
            j += 1
        return num
        
    def t(self,my_deque):
        round_1 = []
        while my_deque:
            t1 = my_deque.popleft()
            if my_deque:
                t2 = my_deque.popleft()
                my_deque.append(t2)
            round_1.append(t1)
        return round_1


        
