class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forb = set(forbidden)
        max_w = max(list(len(i) for i in forbidden))
        def bad():
            temp = ""
            cur_len= len(currunt_element)
            for i in range(1,max_w + 1):
                if cur_len - i < 0:
                    break
                temp = currunt_element[cur_len - i] + temp
                if temp in forb:
                    return True
            return False
        
        currunt_element = deque()
        l = r =res = 0
        while r < len(word):
            currunt_element.append(word[r])
            while bad():
                currunt_element.popleft()
                l += 1
            res = max(res,r - l + 1)
            r += 1
        return res 

