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


        
        self.storage += 1

    def get(self):
        pass


buffer = RingBuffer(3)
buffer.append("petar")
buffer.append("shaun")
buffer.append("luke")
buffer.append("zika")
buffer.append("mile")


print(buffer.storage)
