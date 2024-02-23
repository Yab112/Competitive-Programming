class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue_1,queue_2 = deque(),deque() 

        for i,char in enumerate(senate):
            if char == "D":
                queue_1.append(i)
            else:
                queue_2.append(i)
        p1 = p2 = 0
        n = len(senate)
        while queue_2 and queue_1:
            if queue_2[p2] < queue_1[p1]:
                temp = queue_2.popleft()
                queue_1.popleft()
                n += 1
                queue_2.append(n)
            else :
                temp = queue_1.popleft()
                queue_2.popleft()
                n += 1
                queue_1.append(n)
        return "Dire" if not queue_2 else "Radiant"