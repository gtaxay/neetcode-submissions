class MinStack:
    # want to have min at all times. So keep track of min trhough push and pop

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1], val))
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
