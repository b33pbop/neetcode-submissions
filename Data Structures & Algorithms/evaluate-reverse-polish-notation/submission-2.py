class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack: if operator, pop top 2 from the stack, do the operation then append again
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue
            
            a = stack.pop()
            b = stack.pop()
            if token == "+":
                stack.append(b + a)
            elif token == "-":
                stack.append(b - a)
            elif token == "*":
                stack.append(b * a)
            elif token == "/":
                stack.append(int(b / a))

        return stack[0]