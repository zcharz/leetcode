# idea:
# key : [ (time, val), (time2, val2), ...]
# left most binary search over time+1 to find first instance of time greater


class TimeMap:

    def __init__(self):
        self.times = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = []
        self.times[key].append((timestamp, value))        
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ''
        
        values = self.times[key]
        l, r = 0, len(values)-1

        while l<r:
            mid = (l+r)//2
            if values[mid][0]<timestamp:
                l = mid+1
            else:
                r = mid

        if values[l][0] <= timestamp:
            return values[l][1]
        else:
            return values[l-1][1] if l>0 else ''
        


sol = TimeMap()
sol.set('foo', 'bar', 1)
print(sol.get('foo', 1))
print(sol.get('foo', 3))
sol.set('foo', 'bar2', 4)
print(sol.get('foo', 4))
print(sol.get('foo', 5))
print(sol.times)



sol = TimeMap()
sol.set("love","high",10)
sol.set("love","low",20)
print(sol.get('love', 5))
print(sol.get('love', 10))
print(sol.get('love', 15))
print(sol.get('love', 20))
print(sol.get('love', 25))
print(sol.times)