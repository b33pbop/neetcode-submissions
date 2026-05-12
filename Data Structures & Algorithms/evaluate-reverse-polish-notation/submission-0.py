class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack: if operator, pop top 2 from the stack, do the operation then append again
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
                continue
            
            a = int(stack.pop())
            b = int(stack.pop())
            if token == "+":
                stack.append(b + a)
            elif token == "-":
                stack.append(b - a)
            elif token == "*":
                stack.append(b * a)
            elif token == "/":
                stack.append(int(b / a))

        return int(stack[0])