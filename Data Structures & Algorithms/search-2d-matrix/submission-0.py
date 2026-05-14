class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        matrix = [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ]
        target = 3

        1. Flatten matrix into list then binary search: O(m*n)
        2. Convert (r, h) into a linear index
        -> (0, 0) = 0 * len(row) + col num = 0
        -> (2, 1) = 2 * 4 + 1 = 9
        """

        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            # convert back into coordinates
            x = mid // len(matrix[0])
            y = mid % len(matrix[0])
            
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
