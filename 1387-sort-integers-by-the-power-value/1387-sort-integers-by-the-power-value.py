class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr_1 = []
        arr_2 = []
        for i in range(lo ,hi + 1):
            arr_1.append(i)
            # print(arr_1)
        count = 0
        for num in arr_1:
            while num != 1:
                if num % 2 == 0 :
                    num = num / 2
                else:
                    num = num * 3 + 1
                count += 1
            arr_2.append(count)
            # print(arr_2)
            count = 0
        ziped = [ x for _, x in sorted(zip(arr_2,arr_1))]
        return ziped[k-1]
            
                
        
            
      