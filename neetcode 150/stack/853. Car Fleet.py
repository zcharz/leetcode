class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        input = sorted([(position[i], speed[i]) for i in range(len(position))], key = lambda x: x[0], reverse=True)

        for pos, speed in input:
            time = (target-pos)/speed
            # if current will pass previous, 
            #   then a car further from target is catching up to one closer to target
            #   and joining the fleet
            #   thus the time needs to be updated to the one from the previous (slower)
            #   before being readded
            # else 
            #   add the current one, which is slower than the next car
            #   any car after this that merges with this one will necessarily not catch up to 
            #   any other car or fleet past this one
            if stack and time<=stack[-1]: time = stack.pop()
            stack.append(time)

        return len(stack)


sol = Solution()

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(sol.carFleet(target, position, speed))

target = 10
position = [0,4,2]
speed = [2,1,3]
print(sol.carFleet(target, position, speed))