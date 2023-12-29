from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k_values = []
        n = len(arr)
        for i in range(n-1, 0, -1):
            max_index = self.find_max(arr, i)
            if max_index != i:
                self.flip(arr, max_index)
                k_values.append(max_index + 1)
                self.flip(arr, i)
                k_values.append(i + 1)
        return k_values

    def find_max(self, arr, n):
        maxi = 0
        for i in range(n+1):
            if arr[i] > arr[maxi]:
                maxi = i
        return maxi

    def flip(self, arr, n):
        start = 0
        while start < n:
            temp = arr[start]
            arr[start] = arr[n]
            arr[n] = temp
            start += 1
            n -= 1