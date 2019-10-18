class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    i = self.current

    self.storage[i] = item


  def get(self):
    pass



buffer = RingBuffer(3)
buffer.append('petar')
buffer.append('shaun')
buffer.append('luke')

print(buffer.storage)
