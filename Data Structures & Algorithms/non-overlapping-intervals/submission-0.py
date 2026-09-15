class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [1,2] [2,3] are considered non-overlapping
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            # non-overlapping
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                prevEnd = min(prevEnd, intervals[i][1])
                res += 1
        return res