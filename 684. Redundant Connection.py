# O(n^2) solution
# O(n) iterating through all edges
# O(n) finding the position of each vertice each iteration
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
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


# O(n) union find solution:
# use list of parents and list of ranks for each value n
# when the 2 nodes of an edge have the same parent already, 
# this is a redundant edge

# this solution only only returns the first cycle, not the last

def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    par = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)

    def find(n):
        p = par[n]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p

    # return False if already unioned
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False
        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
        return True
    
    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]

edges = [[1,2],[1,3],[2,3]]
print(findRedundantConnection(edges))