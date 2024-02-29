class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic_s1 = Counter(s1)
        dic_s2 = defaultdict(int)
        l = 0
        for i in range(len(s2)):
            dic_s2[s2[i]] += 1

            if i >= len(s1):
                if dic_s2[s2[l]] == 1:
                    del dic_s2[s2[l]]
                else:
                    dic_s2[s2[l]] -= 1
                l += 1

            if dic_s1 == dic_s2:
                return True

        return False

