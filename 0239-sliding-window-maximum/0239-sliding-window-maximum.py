class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = collections.deque()

        for ind,value in enumerate(nums):

            if queue and ind - k + 1 > queue[0]:
                queue.popleft()
            
            while queue and value > nums[queue[-1]]:
                queue.pop()
            
            queue.append(ind)

            if ind >= k- 1:
                result.append(nums[queue[0]])
        return result