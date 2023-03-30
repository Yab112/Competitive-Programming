# from collections import deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        popped_pointer = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[popped_pointer]:
                print(stack.pop())
                popped_pointer += 1
        return len(stack) == 0
            
        
        