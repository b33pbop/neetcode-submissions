class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack maintains start idx:height
        """
        Update max_area when we are popping from stack
        Input: heights = [2,1,5,6,2,3]
        Output: 10

        stack = [(0, 1), (2, 5), (3, 6)]
        max_area = max(max_area, (i - stack[-1][0]) * stack[-1][1])
        """

        stack = []
        max_area = 0
        i = 0
        
        while i < len(heights):
            node = (i, heights[i])

            while stack and heights[i] < stack[-1][1]:
                max_area = max(max_area, (i - stack[-1][0]) * stack[-1][1])
                top = stack.pop()
                node = (top[0], heights[i])
            
            stack.append(node)
            i += 1

        while stack:
            max_area = max(max_area, (i - stack[-1][0]) * stack[-1][1])
            stack.pop()
        
        return max_area
