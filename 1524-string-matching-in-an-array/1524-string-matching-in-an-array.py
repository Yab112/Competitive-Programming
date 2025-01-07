class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Sort the words by length
        words.sort(key=lambda x: len(x))
        result = []

        # Check if any word is a substring of other longer words
        for i, word in enumerate(words):
            if any(word in other_word for other_word in words[i + 1:]):
                result.append(word)

        return result