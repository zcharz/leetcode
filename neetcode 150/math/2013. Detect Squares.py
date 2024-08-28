from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(px-x) != abs(py-y)) or (x==px and y==py): continue

            if (x, py) in self.points and (px, y) in self.points:
                res += (self.points[(x, y)] * self.points[(x, py)] * self.points[(px, y)])
        return res
    


sol = DetectSquares()
sol.add([3,10])
sol.add([11,2])
sol.add([3,2])
print(sol.count([11,10]))
print(sol.count([14,8]))
sol.add([11,2])
print(sol.count([11,10]))