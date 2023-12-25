class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in digits:
            number = number* 10 + i
        number+= 1
        new_array = []
        while number != 0:
            temp = number % 10
            new_array.append(temp)
            number//=10
        return new_array[::-1]
            
                                