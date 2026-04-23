class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x: x[1])
        cnt=0
        pre=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0] < pre:

                cnt+=1
            else:
                pre=intervals[i][1]

        return cnt

        