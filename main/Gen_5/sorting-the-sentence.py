class Solution:
    def sortSentence(self, s: str) -> str:
        strig = [0]*len(s.split(" "))
        dict_my_dict = {word[-1]: word[:-1] for word in s.split()}
        for number in dict_my_dict.keys():
            strig[int(number) -1] = dict_my_dict[number]
        return  " ".join(strig)
            
        
        