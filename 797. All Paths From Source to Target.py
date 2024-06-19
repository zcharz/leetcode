def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    target = len(graph)-1
    paths = []

    #dfs with a stack
    stack = [(x,[0]) for x in graph[0]]

    while stack != []:
        temp = stack.pop()
        val = temp[0]
        path = temp[1]

        print(temp)

        if val == target:
            path.append(val)
            print('path found: ' + str(path))
            paths.append(path)
        else:
            if val not in path: 
                for node in graph[val]:
                    new = path.copy()
                    new.append(val)
                    stack.append((node, new))
            else:
                pass
                #cycle
        
    return paths


if __name__ == "__main__":
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print('results = ' + str(allPathsSourceTarget(graph)))