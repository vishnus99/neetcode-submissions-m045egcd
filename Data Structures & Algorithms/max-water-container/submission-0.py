class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0

        left, right = 0, len(heights) - 1

        while left < right:
            #area of the container is the smaller height * width
            area = min(heights[left], heights[right]) * (right - left)
            #curr max is the largest between the curr max and the area
            curr_max = max(curr_max, area)

            #if the left side was shorter, increment that side, if the right side was shorter, decrement that side
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return curr_max
            
            