class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights)-1
        max_area = 0
        while p1<p2:
            height1 = heights[p1]
            height2 = heights[p2]
            max_area = max(max_area, (p2-p1)*min(height1 , height2))
            if height1<height2:
                p1+=1
            else:
                p2-=1
        return max_area
        