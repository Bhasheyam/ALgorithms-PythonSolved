def merge(intervals):
        i = 0
        while True:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i]=([intervals[i][0],max(intervals[i][1],intervals[i+1][1])])
                intervals.pop(i+1)
            else:
                i += 1
            if i >= len(intervals)-1:
                break
        return intervals
print merge([ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ])