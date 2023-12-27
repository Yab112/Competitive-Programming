class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_my_dict_1 = {}
        dict_my_dict_2 = {}
        out_put = []
        for num in nums1:
            if num in dict_my_dict_1:
                dict_my_dict_1[num] += 1
            else:
                dict_my_dict_1[num] = 1
        for num in nums2:
            if num in dict_my_dict_2:
                dict_my_dict_2[num] += 1
            else:
                dict_my_dict_2[num] = 1
        for i in nums1:
            if i in nums1 and i in nums2:
                i_in_nums1 = dict_my_dict_1[i]
                i_in_nums2 = dict_my_dict_2[i]
                min_occurance = min(i_in_nums1,i_in_nums2)
                if i not in out_put:
                    out_put.extend([i]*min_occurance)
        return out_put