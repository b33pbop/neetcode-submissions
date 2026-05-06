class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store the difference + the index in a dictioanary
        # e.g. diff = {"4": "0", "3": "1", "2": "2", "1": "3"}
        offset = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            offset[diff] = i

        # iterate nums and check if the value exists in offset with different indices
        for j in range(len(nums)):
            if nums[j] in offset.keys():
                offset_idx = offset.get(nums[j])
                if j != offset_idx:
                    return [j, offset_idx]
        
        return None
            
