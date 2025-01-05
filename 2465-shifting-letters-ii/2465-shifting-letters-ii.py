class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        initial_ = [0] * len(s) 
        n = len(initial_)

        # Process shifts
        for start, end, direction in shifts:
            if direction == 0:  # Left shift
                if start >= 0 and start < n:
                    initial_[start] -= 1
                if end + 1 < n:
                    initial_[end + 1] += 1
            else:  # Right shift
                if start >= 0 and start < n:
                    initial_[start] += 1
                if end + 1 < n:
                    initial_[end + 1] -= 1

        # Compute prefix sum
        pref_sum = [0] * n
        pref_sum[0] = initial_[0]
        for i in range(1, n):
            pref_sum[i] = pref_sum[i - 1] + initial_[i]

        # Apply shifts to the string
        new = ""
        for shift, letter in zip(pref_sum, s):
            start = ord('a')
            new_char = chr((ord(letter) - start + shift) % 26 + start)
            new += new_char

        return new if len(new) == len(s) else new + s[len(new):]