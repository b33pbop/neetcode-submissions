class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointer + prefix, suffix sum approach
        
        prefix_max = []
        suffix_max = []
        total = 0

        for i in range(len(height)):
            j = len(height) - 1 - i
            if i == 0:
                prefix_max.append(height[i])
                suffix_max.append(height[j])
            else:
                prefix_max.append(max(prefix_max[i - 1], height[i]))
                suffix_max.append(max(suffix_max[i - 1], height[j]))

        for i in range(len(height)):
            j = len(height) - 1 - i
            total += min(prefix_max[i], suffix_max[j]) - height[i]

        return total
