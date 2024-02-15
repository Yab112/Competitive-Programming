class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        no_operation = 0
        while target != 1:
            if  target % 2 == 0 and maxDoubles != 0:
                target //= 2
                maxDoubles -= 1
            elif target % 2 == 0 and maxDoubles == 0:
                return no_operation + target - 1
            else:
                target -= 1
            no_operation += 1
        return no_operation
        # 19 18 9 8 4 
        