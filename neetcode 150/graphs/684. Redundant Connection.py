# what does NOT WORK:
# seen = set()
# ret = []
# for v1, v2 in edges:
#     if v1 in seen and v2 in seen:
#         ret = [v1, v2]
#     seen.add(v1)
#     seen.add(v2)
# return ret
# doesnt work because what if (1,2), (3,4), (2,3)?
# then (2,3) is seen as redundant when it's not

# redundant is based on order of edges added to graph
# "last edge that's redundant" doesn't matter because only 1 edge is redundant




class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        pass

    # O(n^2) maybe?? wrote this summer 2023 lol idk
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        ret = None
        subgraphs = []

        for v1, v2 in edges:
            # if condition for new node (non-redundant edge)
            posv1 = None
            posv2 = None
            for i, graph in enumerate(subgraphs):
                if v1 in graph:
                    posv1 = i
                if v2 in graph:
                    posv2 = i
            
            # if both nodes are new
            if posv1 == posv2 == None:
                subgraphs.append([v1, v2])
            # if one node is new
            elif posv1 == None:
                subgraphs[posv2].append(v1)
            elif posv2 == None:
                subgraphs[posv1].append(v2)
            # if both nodes are in different positions
            elif posv1 != posv2:
                subgraphs[posv1].extend(subgraphs[posv2])
                subgraphs.pop(posv2)
            # if both nodes are in the same position already, it is redundant
            else:
                ret = [v1, v2]
        return ret

sol = Solution()

edges = [[1,2],[1,3],[2,3]]
print(sol.findRedundantConnection(edges))

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(sol.findRedundantConnection(edges))