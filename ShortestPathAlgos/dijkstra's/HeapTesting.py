import random
import typing

class Heap():
    def __init__(self, contents, n = -1):
        self.size = n if (n >= 0) else len(contents)
        self.list = contents
        self.heapify()

    def heapify(self):
        if self.size == 0:
            return
        for i in range(self.size):
            self.shuffle(self.size - i - 1)

  ## official PriorityQueue methods begin
    def parentValue(self, i):
        return self.list[(i - 1) // 2]

    def children(self, i):
        return self.list[2 * i + 1], self.list[2 * i + 2]

    def empty(self):
        return self.size == 0

    def swap(self, p, c):
        self.list[p], self.list[c] = self.list[c], self.list[p]

    def put(self, value):
        child = self.size
        self.size += 1
        self.list.append(None)  # increase list size.
        # IMPORTANT: We don't append child because there could be values that have been popped
        self.list[child] = value  # value at index child
        # now fix the heap upwards:
        self.shuffle_up(child)

    def get(self):
        if self.size == 0:
            print("CANNOT DELETE FROM AN EMPTY HEAP")
            return
        max_val = self.list[0]
        # put the last value at the front and then re-sort
        self.list[0] = self.list[self.size - 1]
        self.size -= 1
        self.shuffle(0)
        return max_val

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

    def shuffle_up(self, child):
        while child > 0 and self.list[child] < self.parentValue(child):
            parent = (child - 1) // 2
            self.swap(child, parent)
            child = parent


def bubble_up(data, n, child):
    while child > 0 and data[child] < data[(child - 1) // 2]:
        parent = (child - 1) // 2
        data[child], data[parent] = data[parent], data[child]
        child = parent


def bubble_down(list, n, i):
    parent = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and list[left_child] < list[parent]:
        list[left_child], list[parent] = list[parent], list[left_child]
        bubble_down(list, n, left_child)
    if right_child < n and list[right_child] < list[parent]:
        list[right_child], list[parent] = list[parent], list[right_child]
        bubble_down(list, n, right_child)


def is_heap(l, n):
    if l==None:
        return False
    for i in range(n):
        if 2 * i + 2 < n and l[i] > l[2 * i + 2]:
            return False
        if 2 * i + 1 < n and l[i] > l[2 * i + 1]:
            return False
    return True


def heapify(data, n=-1):
    n = len(data) if n <= 0 else n
    if n == 0:
        return data
    for i in range(len(data)):
        bubble_down(data, n, n - i - 1)
    return data

def test_is_heap_1():
  data = [50, 100, 1000, 150, 2000, 1100, 1200]
  n = len(data)
  assert is_heap(data, n)

def test_is_heap_2_right():
  # right child fails
  data = [50, 100, 1300, 150, 1500, 1600, 1100]
  n = len(data)
  assert not is_heap(data, n)

def test_is_heap_2_left():
  # left child fails
  data = [50, 20, 1000, 150, 1500, 1900, 5200]
  n = len(data)
  assert not is_heap(data, n)

def test_bubble_up_1():
  data = [10,50,500,60,3000,600,45]
  n = 7
  bubble_up(data, n, 6)
  assert is_heap(data,n)

def test_bubble_up_2():
  data    = [10,50,45,60,3000,600,500]
  correct = [10,50,45,60,3000,600,500]
  n = 7
  pos = 2
  bubble_up(data, n, pos)
  assert is_heap(data,n)

def test_bubble_up_3():
  data = [200, 250, 1000, 3000, 1900, 1100, 30]
  correct = [30, 250, 200, 3000, 1900, 1100, 1000]
  n = 7
  pos = 6
  bubble_up(data, n, pos)
  assert data == correct

def test_bubble_down_1():
  data = [3000, 50, 45, 60, 500, 600, 0]
  correct = [45, 50, 600, 60, 500, 3000, 0]
  n = 6
  pos = 0
  bubble_down(data, n, pos)
  assert is_heap(data,n)

def test_heap_1a():
  data = [50, 100, 150, 300]
  correct = [50,100,150, 300, 0, 0 ,0]
  h = Heap(data)
  assert is_heap(h.list, len(data))

def test_heap_1b():
  data = [50, 100, 150]
  correct = [50, 100, 150, 0, 0, 0, 0]
  h = Heap(data)
  assert is_heap(h.list, len(data))

## this is just for testing code - you do not need to understand it
def heap_counterexample_maybe (data: [int], n: int):
    '''Returns the first child found that is a counterexample to the heap property, or False if none such exists.'''
    for p, current in enumerate(data):
        left_child = 2*p+1
        right_child = 2*p+2
        if left_child < n and data[left_child] < current:
            return left_child
        if right_child < n and data[right_child] < current:
            return right_child
    return False

def test_heap_2():
    data = [60, 24, -40, 167, -11, -81, 120, 157, -108, -147]
    n = len(data)
    heap = heapify(data)
    #assert is_heap(heap, n)
    assert heap_counterexample_maybe(heap, n) is False

def test_heap_3():
    for _ in range(100):
        n = random.randint(5,100)
        data = [ random.randint(-1000,1000) for _ in range(n)]
        heap = heapify(data)
        assert is_heap(heap, n)
        ## union with 0 to make sure the padding appears
        assert set(heap).union({0}) == set(data).union({0})

def test_heap_ops_1():
    data = [10,40,100,300,80,150,250]
    h = Heap(data)
    v = h.get()
    assert v == 10
    v = h.get()
    assert v == 40
    v = h.get()
    assert v == 80

def test_heap_ops_2():
    h = Heap([10,40,100,300,80,150])
    h.put(250)
    assert h.list == [10,40,100,300,80,150,250]

def test_heap_ops_3():
    h = Heap([10,40,100,300,80,150])
    h.put(250)
    h.put(20)
    assert is_heap(h.list, len(h.list))
