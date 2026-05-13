class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [2, 5, ]
        # res = [1, 1, 1+1, 1+1, 1, 0, 0, 0]
        """
        pseudocode:
        1. maintain a stack storing the index of temperatures
        2. if new temperature is larger than the top of the stack, we pop
        3. set the index popped to be current idx - popped index
        4. else we do not pop
        """

        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            
            stack.append(i)
        
        return res
