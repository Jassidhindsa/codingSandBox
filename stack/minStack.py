class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append([val, val])
        else:
            minVal = min(self.stack[-1][1], val)
            self.stack.append([val, minVal])
        
    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


if __name__ == "__main__":
    minStack = MinStack();
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())