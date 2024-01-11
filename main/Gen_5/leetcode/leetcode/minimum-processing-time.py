class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks_sorted = sorted(tasks)
        processorTime_sorted = sorted(processorTime,reverse = True)
        l_1= 0 
        l_2 = 0
        r = 3
        holder = []
        max_ = 0
        while r < len(tasks):
            for i in range(l_1,r + 1):
                if tasks_sorted[i] + processorTime_sorted[l_2] > max_:
                    max_ = tasks_sorted[i] + processorTime_sorted[l_2]
            l_2 += 1
            l_1 = r + 1
            r = r + 4
                
         
        return max_