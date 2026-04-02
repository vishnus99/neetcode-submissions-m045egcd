class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        return self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        curr = self.stack[-1]
        for i in self.stack:
            if i >= curr:
                continue
            else: 
                curr = i
        return curr
