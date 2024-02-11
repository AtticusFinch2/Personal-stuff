
class minHeapBM:
    def __init__(self, initial_array=[]):
        self.list = initial_array
        self.size = len(initial_array)
        self.heapify()

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

    def bubble_down(self, i):
        bubble_down(self.list, self.size, i)

    def bubble_up(self, child):
        while child > 0 and self.list[child] < self.parentValue(child):
            parent = (child-1)//2
            self.swap(child, parent)
            child = parent

    def put(self, value):
        child = self.size
        self.size += 1
        self.list.append(None)  # increase list size.
        # IMPORTANT: We don't append child because there could be values that have been popped
        self.list[child] = value  # value at index child
        # now fix the heap upwards:
        self.bubble_up(child)

    def get(self):
        if self.size == 0:
            print("CANNOT DELETE FROM AN EMPTY HEAP")
            return
        max_val = self.list[0]
        # put the last value at the front and then re-sort
        self.list[0] = self.list[self.size-1]
        self.size -= 1
        bubble_down(self.list, self.size, 0)
        return max_val

    def heapify(self):
        if self.size == 0:
            return
        for i in range(self.size):
            bubble_down(self.list, self.size, self.size - i - 1)


def is_min_heap(l):
    n = len(l)
    for i in range(n):
        if 2*i+1 <= n and 2*i+2 <= n:
            if l[i] <= l[2*i+1] and l[i] <= l[2*i+2]:
                return False
        elif 2*i+1 <= n:
            if l[i] <= l[2*i+1]:
                return False
    return True

def bubble_down(list, n , parent):
    left, right = 2*parent+1, 2*parent+2
    if left < n:
        child = left
        if right < n and list[right] < list[left]:
            child = right
        if list[child] < list[parent]:
            list[parent], list[child] = list[child], list[parent]
            bubble_down(list, n, child)

def heapify(inp_list):
    j = minHeapBM(initial_array=inp_list)
    return j.list


'''

queue_before = [10,35,33,42,7,14,19,27,44,26,31]

print(f"Values before insertion into the heap: {queue_before}")
is_inserting = False
if is_inserting:  # O(nlogn)
    heap = minHeapBM()
    for element in queue_before:
        heap.insert(element)
else:  # O(n)
    heap = minHeapBM(initial_array=queue_before)
print("Heap elements before deletion:", end=" ")
heap.printHeap()
top_value = heap.pop()
print("Top element:", top_value)
print("Heap elements after deletion:", end=" ")
heap.printHeap()
heap.destroyHeap()

import copy
neighbor = 6
current = 5
path_to_current = [1,4,5]
d_to_neighbor = 56
heap = minHeapBM(initial_array=[(60, 6, [1, 3, 6]), (70, 6, [1, 2, 6]), (60, 6, [1, 3, 6]), (100, 1, [1, 4, 1]), (70, 6, [1, 2, 6]), (70, 6, [1, 2, 6]), (70, 6, [1, 2, 6]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (70, 6, [1, 2, 6]), (70, 6, [1, 2, 6]), (70, 6, [1, 2, 6]), (70, 6, [1, 2, 6]), (70, 6, [1, 2, 6]), (70, 6, [1, 2, 6]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (70, 6, [1, 2, 6]), (70, 6, [1, 2, 6]), (100, 1, [1, 4, 1]), (70, 6, [1, 2, 6]), (100, 1, [1, 4, 1]), (70, 6, [1, 2, 6]), (100, 1, [1, 4, 1]), (70, 6, [1, 2, 6]), (100, 1, [1, 4, 1]), (70, 6, [1, 2, 6]), (100, 1, [1, 4, 1]), (70, 6, [1, 2, 6]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (100, 1, [1, 4, 1]), (70, 6, [1, 2, 6])])

path_to_neighbor = copy.deepcopy(path_to_current)
path_to_neighbor.append(neighbor)
print(neighbor, current, path_to_neighbor)
heap.insert((d_to_neighbor, neighbor, path_to_neighbor))
print(heap.list)'''