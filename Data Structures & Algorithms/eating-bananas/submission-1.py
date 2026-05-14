class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        minimum h = length of piles
        therefore max k = largest pile
        smallest k = 1
        our sorted array -> k = [1, largest pile] e.g. [1,2,3,4,5,6,7,8,9,10,11]
        since its increments of 1, we dont need an array, each value = idx + 1
        target -> h
        """

        l = 1
        r = max(piles)
        k = 0
        diff = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            time_needed = 0
            for pile in piles:
                time_needed += math.ceil(pile / mid)

            if time_needed <= h:
                k = mid
                r = mid - 1
            elif time_needed > h:
                l = mid + 1

        return k
