class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        suf_sum_y = [0] * len(customers)
        pref_sum_n = [0] * len(customers)
        suf_sum_y[-1] = 1 if customers[-1] == "Y" else 0
        
        for i in range(1,len(customers)):
            zero = 1 if customers[i - 1] == "N" else 0
            one = 1 if customers[n- i - 1] == "Y" else 0
            pref_sum_n[i] =  pref_sum_n[i- 1] + zero
            suf_sum_y[n- i - 1] = suf_sum_y[n- i] + one
            
        pref_sum_n.append(pref_sum_n[-1])
        suf_sum_y.append(0)
        ans = float("inf")
        index = 0
        k = 0
        for i ,j in zip(suf_sum_y,pref_sum_n):
            if i + j < ans:
                ans = i + j
                index = k
            k += 1 
        return index
            
        
                    
                    