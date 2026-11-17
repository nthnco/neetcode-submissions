class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #[[1,3],[1,5],[6,7]]
        1, 3
        1, 5
        """I know that the current element will never be lower than the prev element if I sort it"""
        res = []
        intervals.sort(key=lambda i: i[0])
        res.append(intervals[0])
        for start, end in intervals:
            cur_end = res[-1][1]
            if start <= cur_end:
                res[-1][1] = max(cur_end, end)
            else:
                res.append([start,end])
        return res
            


        
        