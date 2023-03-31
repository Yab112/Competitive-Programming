class Solution:
    def compress(self, chars: List[str]) -> int:
        n, ptr, count = len(chars), 0, 1

        for i in range(1,n+1):

            if i < n and chars[i] == chars[i-1]: count += 1

            else:
                chars[ptr] = chars[i-1]
                ptr+= 1

                if count > 1:
                    s = str(count)
                    m = len(s)
                    chars[ptr : ptr + m] = s
                    ptr+= m
 
                count = 1

        return ptr               
                    
                    
                
           

            
             
    
            