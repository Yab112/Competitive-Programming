class Solution:
    def smallestNumber(self, num: int) -> int:
        minimum = num
        if num == 0:
            return 0
        if num < 0:
            temp = abs(num)
            new_a  = self.nums_to_array(temp)
            new_a.sort(reverse= True)
            new_num = self.join_nums(new_a)
            return -1 * new_num
        new_a  = self.nums_to_array(num)
        new_a.sort()
        new_num = self.join_nums(new_a)
        if new_num < minimum:
            return new_num
        else:
            return minimum
        
        
    def nums_to_array(self,num) -> list:
        array = []
        while num != 0:
            temp = num%10
            array.append(temp)
            num//=10
        return array
    def join_nums(self,jo)->int:
        num_coll = 0
        l = r=0
        while l <= r and jo[r] ==0:
            r += 1
            
        temp = jo[l]
        jo[l] = jo[r]
        jo[r] = temp
        for i in jo:
            num_coll = num_coll * 10 + i
        return num_coll
            
        