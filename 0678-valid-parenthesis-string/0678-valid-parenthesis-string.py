class Solution:
    def checkValidString(self, s: str) -> bool:  
        counter = 0  
        for i in s:  
            if i in "(*": 
                counter += 1 
                 
            elif counter:  
                counter -= 1  
            else:
                return False
        counter = 0
        for i in s[::-1]:  
            if i in "*)": 
                counter += 1 
            elif counter:  
                counter -= 1  
            else:
                return False
        return True
        

     