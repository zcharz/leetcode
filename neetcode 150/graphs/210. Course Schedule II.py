class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        prereqs = {i:set() for i in range(numCourses)}
        for course, pre in prerequisites:
            prereqs[course].add(pre)
        
        visited, path = set(), set()
        ret = []

        def dfs(n):
            # cycle on current path
            if n in path: return False
            # already visited 
            if n in visited: return True

            path.add(n)
            for i in prereqs[n]:
                if not dfs(i): return False
            path.remove(n)

            visited.add(n)
            ret.append(n)
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        return ret



sol = Solution()

numCourses = 2
prerequisites = [[1,0]]

print(sol.findOrder(numCourses, prerequisites))