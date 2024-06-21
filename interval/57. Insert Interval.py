# how to check if intervals DONT overlap:
# if new_end < curr start
# OR
# if new_start > curr_end



def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    ret = []

    for i in range(len(intervals)):
        # the new interval ends before this current one
        # current and all intervals after must be in return
        if newInterval[1] < intervals[i][0]:
            ret.append(newInterval)
            return ret+intervals[i:]
        # new interval starts after current ends
        elif newInterval[0]>intervals[i][1]:
            ret.append(intervals[i])
        # now the intervals must be overlapping
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])

    # new interval must overlap with last interval
    ret.append(newInterval)
    return ret

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))