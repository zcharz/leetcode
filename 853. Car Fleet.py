def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    stack = []
    cars = sorted([ (position[i], speed[i]) for i in range(len(position)) ], key=lambda x: x[0] ) 
    print(cars)

    for i in cars:
        time = float((target-i[0])/i[1])
        print(time)
        
        while stack and time >= stack[-1]:
            time = stack[-1]
            stack.pop()

        stack.append(time)

    print(stack)
    return len(stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

target = 10
position = [0,4,2]
speed = [2,1,3]


print(carFleet(target, position, speed))