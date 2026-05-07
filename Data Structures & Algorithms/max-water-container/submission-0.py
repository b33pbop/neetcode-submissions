class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start with 2 pointers on each end
        # keep moving the smaller one and update the volume
        i = 0
        j = len(heights) - 1
        max_area = 0

        while i != j:
            h = min(heights[i], heights[j])
            max_area = max((j - i) * h, max_area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_area
