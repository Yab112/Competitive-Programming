class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict = {}
        max_ = 0
        for num in nums:
            if num not in my_dict:
                my_dict[num] = [num,num]
                left = num
                right = num
                if num - 1 in my_dict:
                    left = my_dict[num-1][0]
                    
                if num + 1 in my_dict:
                    right = my_dict[num+1][1]
                
                my_dict[left] = [left,right]
                my_dict[right] = [left,right]
                
                max_ = max(max_,right - left + 1)
        return max_


                   
         
            