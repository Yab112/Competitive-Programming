class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        wait = [0] * n
        closest_gt = [n-1]
        for i in xrange(n-2, -1, -1):
            if temperatures[i+1] > temperatures[i]:
                wait[i] = 1
            else:
                while closest_gt:
                    j = closest_gt[-1]
                    if temperatures[j] > temperatures[i]:
                        wait[i] = j - i
                        break
                    else:
                        closest_gt.pop()
            closest_gt.append(i)
        return wait