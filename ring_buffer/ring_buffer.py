class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        if self.current >= self.capacity:
            self.current = 0
        i = self.current
        self.storage[i] = item
        self.current += 1

    def get(self):
        new_list = []
        for item in self.storage:
            if item != None:
                new_list.append(item)

        return new_list
