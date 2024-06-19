
# O(n + p) time iterative dfs solution
# p = len(prereq)
# n = numCourses
# idea: clear courses one at a time, clear them from prereqs of other classes
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    clears = dict()
    prereqs = dict()
    # one course can have multiple prereqs
    # and clear multiple prereqs for diff courses

    need_prereq = set()

    for course, pr in prerequisites:
        need_prereq.add(course)

        if course in prereqs:
            prereqs[course].add(pr)
        else:
            prereqs[course] = {pr}

        if pr in clears:
            clears[pr].add(course)
        else:
            clears[pr] = {course}
    
    stack = [ i for i in range(numCourses) if i not in need_prereq]
    count = 0

    while stack:
        curr = stack.pop()
        count+=1

        # if current doesn't clear any courses
        if curr not in clears:
            continue

        # for each course that curr is a prereq of, 
        # remove curr from their prereq list
        for cleared in clears[curr]:
            if cleared not in prereqs:
                continue

            prereqs[cleared].remove(curr)

            # if there are no more prereqs for a class, add it
            if len(prereqs[cleared])==0:
                stack.append(cleared)

    if count==numCourses:
        return True
    return False


# neetcode recursive dfs solution
# idea: using cycle detection to detect if a class can't be completed
# clearing courses if they are known to be completable to shorten runtime
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # dfs
    preMap = {i: [] for i in range(numCourses)}

    # map each course to : prereq list
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visiting = set()

    def dfs(crs):
        if crs in visiting:
            return False
        if preMap[crs] == []:
            return True

        visiting.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visiting.remove(crs)
        preMap[crs] = []
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False
    return True



numCourses = 2
prerequisites = [[1,0]]

numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
# expected = True

print(canFinish(numCourses, prerequisites))