class MinStack:
    # each node in the stack will be a tuple of (val, smallest up to that node)

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        cur_min = self.stack[-1][1] if self.stack else float('inf')
        node = (val, min(cur_min, val))
        self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else float('inf')
