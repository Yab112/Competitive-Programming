from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
        our_dic = defaultdict(lambda:0)
        
        for i in cpdomains:
                temp = i.split(" ")
                temp2 = temp[1].split(".")
                if len(temp2) == 3:
                        lv_1 = temp[1]
                        our_dic[lv_1] += int(temp[0])
                        lv_2 = ".".join(temp2[1:])
                        our_dic[lv_2] += int(temp[0])
                        lv_3 =temp2[-1]
                        our_dic[lv_3] += int(temp[0])
                else:
                        lv_1 = temp[1]
                        our_dic[lv_1] += int(temp[0])
                        lv_3 = lv_3 =temp2[-1]
                        our_dic[lv_3] += int(temp[0])
        return [str(j) + " " + i for i,j in our_dic.items()]
                
                
                        
