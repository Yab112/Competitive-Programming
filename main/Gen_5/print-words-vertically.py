class Solution:
    def printVertically(self, s: str) -> List[str]:
        word_in_list = s.split()
        max_word = 0
        vertical = []
        for i in word_in_list:
            if int(len(i)) > max_word:
                max_word = len(i)
        for i in range(max_word):
            temp = ""
            for word in word_in_list:
                if i > len(word) - 1:
                    temp += " "
                else:
                    temp += word[i]
            vertical.append(temp)
       
        return [vertical_words.rstrip() for vertical_words in vertical]
            
            
            
     
        