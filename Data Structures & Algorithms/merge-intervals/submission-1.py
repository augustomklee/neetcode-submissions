class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prevInterval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] > prevInterval[1]:
                res.append(prevInterval)
                prevInterval = intervals[i]
            if prevInterval[1] >= intervals[i][0]:
                prevInterval = [
                    min(prevInterval[0], intervals[i][0]),
                    max(prevInterval[1], intervals[i][1])
                ]
        res.append(prevInterval)
        return res            
            
