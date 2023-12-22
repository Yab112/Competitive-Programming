class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        no_good_pair = 0
        my_dict = {}
        for index, value in enumerate(nums):
            if value not in my_dict:
                my_dict[value] = []
            my_dict[value].append(index)

        for m,i in enumerate(nums):
            if i in my_dict:
                for j in my_dict[i]:
                    if m < j and (m * j) % k == 0: 
                        no_good_pair += 1
        return no_good_pair