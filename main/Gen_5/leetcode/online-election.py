class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.dic = defaultdict(int)
        self.winner = []
        self.cur_max = -1
        self.cur_elem = self.persons[0]
        for i in self.persons:
            self.dic[i] += 1
            if self.cur_max <= self.dic[i]:
                self.cur_max = self.dic[i]
                self.cur_elem = i
            self.winner.append(self.cur_elem)

    def q(self, t: int) -> int:
        def find_pos(times,target):
            l  =  - 1
            r =  len(times)
            while r - l > 1:
                mid = l + ( r - l) // 2
                if times[mid] > target:
                    r = mid 
                else:
                    l = mid 
            return l
        pos = find_pos(self.times ,t ) 

        return self.winner[pos]

