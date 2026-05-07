class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # iterate left to right and right to left
        # each element from left to right would be the product of its previous elements
        # E.g. [a, b, c, d] -> LtR: [1, a, ab, abc], RtL: [bcd, cd, d, 1]
        # Then multiply both lists element wise with each other

        # arrays to store cummulative product
        left_to_right = [1] * len(nums)
        right_to_left = [1] * len(nums)
        cum_prod_left = 1
        cum_prod_right = 1

        for i in range(len(nums)):
            j = len(nums) - 1 - i # pointer to the end
            left_to_right[i] = cum_prod_left
            right_to_left[j] = cum_prod_right
            cum_prod_left *= nums[i]
            cum_prod_right *= nums[j]
            
        # multiply and store in left_to_right
        for j in range(len(left_to_right)):
            left_to_right[j] *= right_to_left[j]

        return left_to_right
