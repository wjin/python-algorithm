class Queue:
    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)

    def pop(self):
        if len(self._data) == 0:
            raise IndexError
        self._data.pop(0)

    def front(self):
        if len(self._data) == 0:
            raise IndexError
        return self._data[0]

    def back(self):
        if len(self._data) == 0:
            raise IndexError
        return self._data[-1]

    def empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def dump(self):
        while not self.empty():
            print self.front()
            self.pop()

if __name__ == "__main__":
    que = Queue()

    que.push(1)
    que.push(2)
    que.push(3)

    print que.size()
    print que.front()
    print que.back()

    que.dump()
    print que.size()
    #que.pop()
