class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        yab = [0] * (len(nums) + 1)

        for i in range(1, len(yab)):
            yab[i] = yab[i - 1] + nums[i - 1]

        res = len(nums) + 1
        #
        Q = collections.deque()

        for i in range(len(yab)):
            while Q and yab[i] - yab[Q[0]] >= k:
                res = min(res, i - Q.popleft())
            while Q and yab[i] < yab[Q[-1]]:
                Q.pop() # pop right
            Q.append(i)

        return res if res != len(nums)+1 else -1
