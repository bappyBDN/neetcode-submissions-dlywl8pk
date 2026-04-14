class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        max_Area=0
        for i in range(n):
            for j in range(i+1,n):
                c=1
                h=min(heights[i],heights[j])
                d=j-i
                c=h*d
                max_Area=max(c,max_Area)
        return max_Area



        