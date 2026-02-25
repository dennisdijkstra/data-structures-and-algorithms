class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def size(self):
        return self.size

    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def pop(self):
        self.stack.pop()
        self.size -= 1

    def peek(self):
        if self.is_empty():
            return None

        return self.stack[-1]

    def is_empty(self):
        return self.size == 0
