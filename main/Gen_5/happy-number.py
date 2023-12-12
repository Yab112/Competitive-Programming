class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        number = n
        result = 0
        my_set = set()
        while n!= 1 :
            temp = 0
            list_  = return_number_list(n) 
            for i in range(len(list_)):
                temp += list_[i] ** 2
            n = temp
            if n in my_set:
               return False
            my_set.add(n)
        return True
def return_number_list(n):
    array_num = []
    while n !=0:
        temp = n % 10
        array_num.append(temp)
        n //= 10
    return array_num