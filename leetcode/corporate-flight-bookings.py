class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] *( n + 4)

        for start ,end,seat in bookings:
            seats[start - 1] += seat
            seats[end] -= seat
        pref_sum = list(accumulate(seats))

        return pref_sum[:n]
 


        