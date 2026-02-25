import math


class Heap:
    def __init__(self, comparator):
        self.heap = []
        self.comparator = comparator

    def build(self, list):
        self.heap = list
        last_parent_index = self.get_parent_index(len(self.heap) - 1)

        for index in range(last_parent_index, -1, -1):
            self.heapify_down(index)

    def add(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def peek(self):
        if len(self.heap) == 0:
            return None

        return self.heap[0]

    def remove(self):
        if len(self.heap) == 0:
            return None

        self.swap(0, len(self.heap) - 1)
        self.heap.pop()
        self.heapify_down(0)

    def heapify_down(self, index):
        left_child_index = self.get_child_index(index, 1)

        while left_child_index != -1:
            smallest_child_index = left_child_index
            right_child_index = self.get_child_index(index, 2)

            if right_child_index != -1 and self.comparator(
                self.heap[right_child_index], self.heap[left_child_index]
            ):
                smallest_child_index = right_child_index

            if self.comparator(self.heap[smallest_child_index], self.heap[index]):
                self.swap(smallest_child_index, index)
                index = smallest_child_index
                left_child_index = self.get_child_index(index, 1)
            else:
                break

    def heapify_up(self, index):
        parent_index = self.get_parent_index(index)

        while index > 0 and self.comparator(self.heap[index], self.heap[parent_index]):
            self.swap(index, parent_index)
            index = parent_index
            parent_index = self.get_parent_index(index)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def get_child_index(self, parent_index, child_number):
        child_index = (parent_index * 2) + child_number
        last_index = len(self.heap) - 1

        return child_index > last_index and -1 or child_index

    def get_parent_index(self, child_index):
        return math.floor((child_index - 1) / 2)
