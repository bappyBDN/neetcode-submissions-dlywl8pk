class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l=0
        r=n-1
        max_Area=0
        while l <r:
            area=min(heights[l],heights[r])*(r-l)
            max_Area=max(max_Area,area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return max_Area





        