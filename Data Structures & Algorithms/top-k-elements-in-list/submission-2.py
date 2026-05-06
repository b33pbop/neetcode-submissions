class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force: make a freq array and sort it in descending order

        # bucket sort
        # create frequency array
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # create buckets of size n
        buckets = list()
        n = len(nums)

        # initialize buckets with lists
        for i in range(n + 1):
            buckets.append([])

        # using the frequency of a number as the bucket index, append to the correct bucket
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        result = []

        # loop from the end to get top k
        for i in range(n, -1, -1):
            if len(buckets[i]) == 0:
                continue

            for j in range(len(buckets[i]) - 1, -1, -1):
                if k == 0:
                    break
                # append the value in the bucket
                result.append(buckets[i][j])
                k -= 1
            
        return result
