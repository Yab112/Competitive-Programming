class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        white = 0
        minim = len(blocks)
        if k == len(blocks):
            return blocks.count("W")
        if "B" * k in blocks:
            return 0
        for i in range(len(blocks)):
            right_char = blocks[i]
            if right_char == "W":
                white +=1
            if i - l + 1 == k:
                minim = min(minim,white)
                left_char  = blocks[l]
                if left_char == "W":
                    white -= 1
            
                l += 1
        return minim
    
    
    
    
   



