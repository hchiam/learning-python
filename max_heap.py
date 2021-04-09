import heapq


class Heap():
    def __init__(self):
        self.heap = []
        heapq._heapify_max(self.heap)

    def add(self, value):
        heapq.heappush(self.heap, value)
        heapq._heapify_max(self.heap)

    def pop(self):
        if len(self.heap) == 0:
            return None
        output = heapq.heappop(self.heap)
        heapq._heapify_max(self.heap)
        return output

    def top(self):
        return self.heap[0] if len(self.heap) else None

    def get_heap(self):
        return self.heap


# demo:

h = Heap()
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

h.add(1)
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

h.add(2)
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

h.add(3)
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

print(h.pop())
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

print(h.pop())
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

print(h.pop())
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

h.add(3)
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

h.add(1)
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

h.add(4)
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

h.add(7)
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

h.add(5)
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

h.add(10)
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

print(h.pop())
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

print(h.pop())
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

print(h.pop())
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

print(h.pop())
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

print(h.pop())
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

print(h.pop())
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())

print(h.pop())
print('\033[94m(' + str(h.top()) + ')\033[0m', h.get_heap())
