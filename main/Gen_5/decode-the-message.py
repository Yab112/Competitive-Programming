class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        my_dict = {}
        yab = "".join((key.split()))
        number = range(ord('a'),ord('z') + 1)
        counter = 0
        for i in yab:
            if i  in my_dict:
                continue
            else:
                my_dict[i] = chr(number[counter])
                counter += 1
        new_str = ""
        for i in message:
            if i == " ":
                new_str += " "
            else:
                temp = " "
                for j in i:
                    temp += my_dict[j]
                new_str += temp.strip()
        return new_str
                    
                
        