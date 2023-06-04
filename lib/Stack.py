class Stack:

    def __init__(self, items = [], limit = 100):
        self.limit = limit
        self.items = items

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            return None
        else:
            return self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1
