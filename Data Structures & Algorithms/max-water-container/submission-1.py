class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        max_w = 0

        while l < r :
            max_c = min(heights[l],heights[r]) * (r - l)
            if max_c > max_w:
                max_w = max_c
            
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return max_w