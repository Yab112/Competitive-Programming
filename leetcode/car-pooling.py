class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_len_road = 1009
        road = [0] * max_len_road

        for n_p , st, end in trips:
            road[st] += n_p
            road[end] -= n_p

        pref_sum = list(accumulate(road))

        return max(pref_sum) <= capacity
   
