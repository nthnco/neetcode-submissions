class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #[[1,2],[3,5],[6,8],[9,10]] [6,7]
        n = len(intervals)
        i = 0
        res = []
        while i < n and intervals[i][1] < newInterval[0]:
            res.append([intervals[i][0],intervals[i][1]])
            i += 1
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)
        while i < n:
            res.append([intervals[i][0], intervals[i][1]])
            i += 1

        return res
        
                
