class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if Counter(ransomNote) & Counter(magazine) == Counter(ransomNote): return True
        return False

            
        
        