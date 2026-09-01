class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        curr = 0

        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
            elif token == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left+right)
            elif token == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left-right)
            elif token == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
            elif token == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
        curr = stack.pop()
        return curr
