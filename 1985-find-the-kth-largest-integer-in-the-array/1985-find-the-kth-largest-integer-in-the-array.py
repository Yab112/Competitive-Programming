import queue
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        pq = queue.PriorityQueue()
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        for i in nums:
            pq.put((-i,i))
        mini= float("inf")
        for i in range(k):
            temp = pq.get()
            print(temp)
            mini = min(mini,temp[1])
        return str(mini)
        
        
        
        