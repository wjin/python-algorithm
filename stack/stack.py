class Stack:
    def __init__(self):
        self._data = []
        self._top = -1

    def push(self, val):
        self._data.append(val)
        self._top += 1

    def pop(self):
        if self._top == -1:
            raise IndexError
        self._data.pop()
        self._top -= 1

    def top(self):
        if self._top == -1:
            raise IndexError
        return self._data[self._top]

    def empty(self):
        return self._top == -1

    def size(self):
        return self._top + 1

    def dump(self):
        while self._top != -1:
            print self.top()
            self.pop()

if __name__ == "__main__":
    stk = Stack()

    stk.push(1)
    stk.push(2)
    stk.push(3)

    print stk.size()
    stk.dump()
    print stk.size()
    #stk.pop()
