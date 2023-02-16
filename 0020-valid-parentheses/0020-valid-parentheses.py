
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=deque()
        charactors={"(":")","[":"]","{":"}"}
        for i in s:
            if i in charactors.keys():
                stack.append(i)
        
            elif len(stack) == 0 or i !=charactors[stack.pop()]:
                return False
        return len(stack) == 0