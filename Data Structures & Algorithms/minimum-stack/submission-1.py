class MinStack:
    # each node in the stack will be a tuple of (val, smallest up to that node)

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.min_val = min(self.min_val, val)
        node = (val, self.min_val)
        self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()
        self.min_val = self.stack[-1][1] if len(self.stack) > 0 else float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min_val
