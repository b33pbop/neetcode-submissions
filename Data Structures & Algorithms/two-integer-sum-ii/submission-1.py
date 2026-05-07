class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers are non decreasing
        # double pointer, move front pointer if sum < target
        # move back pointer if sum > target

        i = 0
        j = len(numbers) - 1

        while i != j:
            if numbers[i] + numbers[j] == target:
                break
            
            elif numbers[i] + numbers[j] < target:
                i += 1

            else:
                j -= 1

        return [i + 1, j + 1]
