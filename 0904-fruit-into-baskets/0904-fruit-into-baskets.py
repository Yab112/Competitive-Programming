class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        lp ,total, max_ = 0 , 0 ,0
        dict_ = collections.defaultdict(int)
        for i in range(len(fruits)):
            dict_[fruits[i]] += 1
            total += 1
            while len(dict_) > 2 :
                test = fruits[lp]
                dict_[test] -=1
                total -= 1
                lp += 1
                if not dict_[test]:
                    dict_.pop(test)
            max_ = max(max_,total)
        return max_        
        
       

        
        

                   
            