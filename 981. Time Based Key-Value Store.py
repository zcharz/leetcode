class TimeMap:

    def __init__(self):
        self.arr = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp>len(self.arr):
            self.arr.extend([[] for i in range(timestamp-len(self.arr))])
        self.arr[timestamp].append((key, value))

    def get(self, key: str, timestamp: int) -> str:
        ret = ''
        
        for 


        return ret





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)



obj = TimeMap()
obj.set(key,value,timestamp)