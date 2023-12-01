class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict_my_dict = {char: i for i, char in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            for j in range(min(len(word1), len(word2))):
                if dict_my_dict[word1[j]] < dict_my_dict[word2[j]]:
                    break
                elif dict_my_dict[word1[j]] > dict_my_dict[word2[j]]:
                    return False
            else:
                if len(word1) > len(word2):
                    return False
        
        return True

