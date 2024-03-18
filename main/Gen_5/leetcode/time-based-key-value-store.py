class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value,timestamp])
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""

        arr = self.dic[key]
        left, right = 0, len(arr) - 1
        result = ""

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                result = arr[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result




# ["TimeMap","set","get","set","set","get","get","set","get"]

# [[],["robb","talisa",2],["robb",3],["sansa", "tyrion",3],["sansa","ramsay",5],["sansa",5],["sansa",1],["bran","bro2",6],["bran",7]]

# robb :[[talisa,2],],sansa:[[trion,3],[ramsay,5]]
# null null talisa  nul null ramsy ""  null bro2