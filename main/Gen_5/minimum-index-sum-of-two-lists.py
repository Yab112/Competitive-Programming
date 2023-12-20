class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minimum = float('inf')
        minim_index = []
        numbers = []
        dict1 = {i:j for j,i in enumerate(list1)}
        for i,k in enumerate(list2):
              if k in dict1:
                  minim_index.append((k,i + dict1[k]))
                  numbers.append(i + dict1[k])
        return [i for i, j in minim_index if j == min(numbers) ]
            