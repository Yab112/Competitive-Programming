class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def back_track(left,right):
            if left > right:
                return 0,0
            curunt_num1,num_next_left = back_track(left + 1,right)
            curunt_num2,num_next_right= back_track(left ,right - 1)
            if nums[left] + num_next_left > nums[right] + num_next_right:
                return nums[left] + num_next_left,curunt_num1
            return nums[right] + num_next_right,curunt_num2
        player1,player2 = back_track(0,len(nums) - 1)
        return player1 >= player2