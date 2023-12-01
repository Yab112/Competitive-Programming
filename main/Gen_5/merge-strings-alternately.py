class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        store = ""
        for i,j in zip(word1,word2):
            store += i + j
        if len(word1) < len(word2):
            store += word2[len(word1):]
        
        if len(word1) > len(word2):
            store += word1[len(word2):]
        return store