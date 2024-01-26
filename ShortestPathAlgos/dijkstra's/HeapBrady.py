class maxHeapBM:
    def __init__(self):
        self.list = []
        self.size = 0

    def printHeap(self):
        print([self.list[i] for i in range(self.size)])

    def destroyHeap(self):
        self.list = []
        self.size = 0

    def swap(self, p, c):
        self.list[p], self.list[c] = self.list[c], self.list[p]

    def parentValue(self, i):
        return self.list[(i-1) // 2]

    def children(self, i):
        return self.list[2 * i + 1], self.list[2 * i + 2]

    def shuffle(self, i):
        parent = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < self.size and self.list[left_child] > self.list[parent]:
            self.swap(parent, left_child)
            self.shuffle(left_child)
        if right_child < self.size and self.list[right_child] > self.list[parent]:
            self.swap(parent, right_child)
            self.shuffle(right_child)

    def insert(self, value):
        child = self.size
        self.size += 1
        self.list.append(value)  # value at index child
        # now fix the heap upwards:
        while child > 0 and self.list[child] > self.parentValue(child):
            parent = (child-1)//2
            self.swap(child, parent)
            child = parent

    def empty(self):
        return self.size == 0

    def pop(self):
        if self.size == 0:
            print("CANNOT DELETE FROM AN EMPTY HEAP")
            return
        max_val = self.list[0]
        # put the last value at the front and then re-sort
        self.list[0] = self.list.pop()
        self.size -= 1
        self.shuffle(0)
        return max_val


class minHeapBM:
    def __init__(self):
        self.list = []
        self.size = 0

    def printHeap(self):
        print([self.list[i] for i in range(self.size)])

    def destroyHeap(self):
        self.list = []
        self.size = 0

    def swap(self, p, c):
        self.list[p], self.list[c] = self.list[c], self.list[p]

    def parentValue(self, i):
        return self.list[(i-1) // 2]

    def children(self, i):
        return self.list[2 * i + 1], self.list[2 * i + 2]

    def empty(self):
        return self.size == 0

    def shuffle(self, i):
        parent = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < self.size and self.list[left_child] < self.list[parent]:
            self.swap(parent, left_child)
            self.shuffle(left_child)
        if right_child < self.size and self.list[right_child] < self.list[parent]:
            self.swap(parent, right_child)
            self.shuffle(right_child)

    def insert(self, value):
        child = self.size
        self.size += 1
        self.list.append(value)  # value at index child
        # now fix the heap upwards:
        while child > 0 and self.list[child] < self.parentValue(child):
            parent = (child-1)//2
            self.swap(child, parent)
            child = parent

    def pop(self):
        if self.size == 0:
            print("CANNOT DELETE FROM AN EMPTY HEAP")
            return
        max_val = self.list[0]
        # put the last value at the front and then re-sort
        self.list[0] = self.list[self.size-1]
        self.size -= 1
        self.shuffle(0)
        return max_val


'''
queue_before = [10,35,33,42,10,14,19,27,44,26,31]
heap = maxHeapBM()
print(f"Values before insertion into the heap: {queue_before}")
for element in queue_before:
    heap.insert(element)
print("Heap elements before deletion:", end=" ")
heap.printHeap()
top_value = heap.pop()
print("Top element:", top_value)
print("Heap elements after deletion:", end=" ")
heap.printHeap()
heap.destroyHeap()
'''