# DIRECTED GRAPH

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacency = { i:[] for i in range(numCourses) }
        for course, prereq in prerequisites:
            adjacency[course].append(prereq)
        seen = set()

        def dfs(curr):
            if curr in seen: return False
            if adjacency[curr] == []: return True

            seen.add(curr)
            for prereq in adjacency[curr]:
                if not dfs(prereq): return False
            seen.remove(curr)

            adjacency[curr] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True

    
sol = Solution()

numCourses = 2
prerequisites = [[1,0]]
print(sol.canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(sol.canFinish(numCourses, prerequisites))

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.canFinish(numCourses, prerequisites))