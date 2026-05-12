class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        [1, 2, 1, 4, 0, 2, 1], k = 3
        [1, 2, 1] -> [2, 1, 1] heap
        iteration 0:
            [1, 2, 1]
            heap: [2, 1, 1]
            removed: []
            max = 2
        iteration 1:
            shift l before right
            [2, 1] -> remove from max heap if its the max
            removed: [1]
            [2, 1, 4] -> add 0 to max heap 
            heap: [4, 2, 1, 1]
            max = 4
        iteration 2:
            shift l before right
            [1, 4] -> remove from max heap if its the max
            [1, 4, 0] -> add 0 to max heap 
            heap: [4, 2, 1, 1, 0]
            removed: [1, 2]
            max = 4
        iteration 3:
            shift l before right
            [4, 0] -> remove from max heap if its the max
            [4, 0, 2] -> add 0 to max heap 
            heap: [4, 2, 2, 1, 1, 0]
            removed: [1, 2, 1]
            max = 4
        iteration 4:
            shift l before right
            [0, 2] -> remove from max heap if its the max
            [0, 2, 1] -> add 0 to max heap 
            heap: [4, 2, 2, 1, 1, 0]
            removed: [1, 2, 1, 4]
            if max of the heap is in removed, we keep popping
            heap: [2, 1, 1, 0]
            removed: [1, 1]
            max = 2
        """

        h = []
        removed = []
        result = []

        l = 0
        r = 0
        while r < k:
            h.append(nums[r])
            r += 1

        heapq.heapify_max(h)
        while r < len(nums):
            while h[0] in removed:
                top = heapq.heappop_max(h)
                removed.remove(top)

            result.append(h[0])
            heapq.heappush_max(h, nums[r])
            
            removed.append(nums[l])
            l += 1
            r += 1

        while h[0] in removed:
            top = heapq.heappop_max(h)
            removed.remove(top)

        result.append(h[0])            

        return result
