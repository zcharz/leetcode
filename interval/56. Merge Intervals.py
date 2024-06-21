# sorting method:
# once sorted, find break point
# break point indicates where an interval starts and ends

# modified merge sort:
# divide and sort, each step also merge when applicable
# each step merging -> o(n)
# since each step is already sorting, time complexity doesn't change
# log n recursive calls


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    ret = []

    currmin = intervals[0][0]
    currmax = intervals[0][1]

    for i in intervals:
        if i[0]>currmax:
            ret.append( [currmin, currmax] )
            currmin = i[0]
            currmax = i[1]
        else:
            currmax = max(currmax, i[1])
    ret.append( [currmin, currmax] )
    return ret


intervals = [[1,3],[8,10],[15,18],[2,6]]
# intervals = [[1,4],[0,2],[3,5]]
print(merge(intervals))
