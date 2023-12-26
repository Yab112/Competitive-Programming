class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new_array = []
        counter_value = collections.Counter(arr1)
        for i in arr2:
            new_array.extend([i]*counter_value[i])
        elemts_left = sorted(list( set(arr1) - set(arr2)))
        for i in elemts_left:
            new_array.extend([i]*counter_value[i])
        return new_array
