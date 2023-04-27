class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        store = []
        ss1 = s1.split()
        ss2 =  s2.split()
        fre1 ,fre2 = {},{} 
        for i in ss1:
            if i not in fre1 :
                fre1[i] = 1 
            else : 
                fre1[i] += 1
        for i in ss2:
            if i not in fre2 :
                fre2[i] = 1 
            else : 
                fre2[i] += 1  
        for k in ss1:
            if k not in fre2 and k not in store and fre1[k] == 1:
                store.append(k)
        for i in ss2:
            if i not in fre1 and i not in store  and fre2[i] == 1:
                store.append(i)
        return store
        