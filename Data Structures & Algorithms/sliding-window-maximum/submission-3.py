class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        For each new element, we remove everything from deque 
        that is smaller than the new element
        [1, 2, 1, 4, 0, 2, 1], k = 3
        
        r = 0, l = 0 -> q = [0], res = []
        r = 1, l = 0 -> q = [1], res = []
        r = 2, l = 0 -> q = [1, 2], res = [nums[1]]
        r = 3, l = r - k + 1 = 1 -> q = [3], res = [nums[1], nums[3]]
        r = 4, l = 2 -> q = [3, 4], res = [nums[1], nums[3], nums[3]]
        r = 5, l = 3 -> q = [3, 5], res = [nums[1], nums[3], nums[3], nums[3]]
        r = 6, l = 4 -> if q[0] == l - 1: popleft on q -> q = [5, 6], res = [nums[1], nums[3], nums[3], nums[3], nums[5]]
        """
        q = deque()
        res = []

        for r in range(len(nums)):
            while len(q) > 0 and nums[r] > nums[q[-1]]:
                q.pop()
            
            q.append(r)

            l = r - k + 1
            if l >= 0:
                while q[0] == l - 1:
                    q.popleft()
                
                res.append(nums[q[0]])
        
        return res
            