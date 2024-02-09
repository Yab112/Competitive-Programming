class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l =team= 0
        r = len(skill) - 1
        check = skill[l] + skill[r]
        flag = True
        while l < r :
            if skill[r] + skill[l] == check:
                team += skill[r] * skill[l]
            else:
                flag= False
                break
            r -= 1
            l += 1
        return team if flag else -1