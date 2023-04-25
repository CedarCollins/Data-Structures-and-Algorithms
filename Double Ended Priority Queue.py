"""
Implements a Double Ended Priority Queue by using a Binary Min Max Heap
"""

import math

class Binary_Min_Max_Heap:

    def __init__(self, alist):
        self.heap = []
        self.build_binary_min_max_heap(alist)

    def is_min_level(self, i):
        level = int(math.log(i+1, 2))
        if level%2 == 0:
            return True
        else:
            return False

    def grandparent(self, i):
        return self.heap[(((i-1)//2)-1)//2]
            
    def parent(self, i):
        return self.heap[(i-1)//2]

    def left_child(self, i):
        return self.heap[2*i+1]

    def right_child(self, i):
        return self.heap[2*i+2]

    def has_left_child(self, i):
        if len(self.heap)-1 >= 2*i + 1:
            return True
        else:
            return False

    def has_right_child(self, i):
        if len(self.heap)-1 >= 2*i + 2:
            return True
        else:
            return False

    def has_children(self, i):
        if self.has_left_child(i) or self.has_right_child(i):
            return True
        else:
            return False

    def has_parent(self, i):
        if i >= 1:
            return True
        else:
            return False

    def has_grandparent(self, i):
        if i >= 3:
            return True
        else:
            return False

    def existing_indices(self, i):
        index_list = []
        if self.has_left_child(i):
            index_list.append(2*i+1)
            if self.has_left_child(2*i+1): #LL Grandchild
                index_list.append(2*(2*i+1)+1)
            if self.has_right_child(2*i+1): #LR Grandchild
                index_list.append(2*(2*i+1)+2)
        if self.has_right_child(i):
            index_list.append(2*i+2)
            if self.has_left_child(2*i+2): #RL Grandchild
                index_list.append(2*(2*i+2)+1)
            if self.has_right_child(2*i+2): #RR Grandchild
                index_list.append(2*(2*i+2)+2)
        return tuple(index_list)

    def index_smallest_child_or_grandchild(self, i):
        index_tuple = self.existing_indices(i)
        children = []
        for index in index_tuple:
            children.append(self.heap[index])
        return index_tuple[children.index(min(children))]    

    def index_largest_child_or_grandchild(self, i):
        index_tuple = self.existing_indices(i)
        children = []
        for index in index_tuple:
            children.append(self.heap[index])
        return index_tuple[children.index(max(children))]

    def push_down_min(self, m):
        if self.has_children(m):
            i = self.index_smallest_child_or_grandchild(m)
            if (i-1)//2 != m: #i is not a child of m (i is a grandchild of m)
                if self.heap[i] < self.heap[m]:
                    self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
                    if self.heap[i] > self.parent(i):
                        self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
                    self.push_down(i)
            elif self.heap[i] < self.heap[m]: #i is a child of m
                self.heap[i], self.heap[m] = self.heap[m], self.heap[i]

    def push_down_max(self, m):
        if self.has_children(m):
            i = self.index_largest_child_or_grandchild(m)
            if (i-1)//2 != m: #i is not a child of m (i is a grandchild of m)
                if self.heap[i] > self.heap[m]:
                    self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
                    if self.heap[i] < self.parent(i):
                        self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
                    self.push_down(i)
            elif self.heap[i] > self.heap[m]: #i is a child of m
                self.heap[i], self.heap[m] = self.heap[m], self.heap[i]

    def push_down(self, i):
        if self.is_min_level(i):
            self.push_down_min(i)
        else:
            self.push_down_max(i)

    def push_up_min(self, i):
        if self.has_grandparent(i) and self.heap[i] < self.grandparent(i):
            self.heap[i], self.heap[(((i-1)//2)-1)//2] = self.heap[(((i-1)//2)-1)//2], self.heap[i]
            self.push_up_min((((i-1)//2)-1)//2)

    def push_up_max(self, i):
        if self.has_grandparent(i) and self.heap[i] > self.grandparent(i):
            self.heap[i], self.heap[(((i-1)//2)-1)//2] = self.heap[(((i-1)//2)-1)//2], self.heap[i]
            self.push_up_max((((i-1)//2)-1)//2)

    def push_up(self, i):
        if i != 0:
            if self.is_min_level(i):
                if self.heap[i] > self.parent(i):
                    self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
                    self.push_up_max((i-1)//2)
                else:
                    self.push_up_min(i)
            else:
                if self.heap[i] < self.parent(i):
                    self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
                    self.push_up_min((i-1)//2)
                else:
                    self.push_up_max(i)

    def insert(self, i):
        self.heap.append(i)
        self.push_up(len(self.heap)-1)

    def find_min(self):
        if len(self.heap) >= 1:
            return self.heap[0]
        else:
            raise ValueError('heap is empty')

    def find_max(self):
        if len(self.heap) >= 3:
            return max(self.heap[1], self.heap[2])
        elif len(self.heap) == 2:
            return self.heap[1]
        elif len(self.heap) == 1:
            return self.heap[0]
        else:
            raise ValueError('heap is empty')

    def remove_min(self):
        if len(self.heap) >= 1:
            self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
            minimum = self.heap.pop()
            self.push_down(0)
            return minimum
        else:
            raise ValueError('heap is empty')

    def remove_max(self):
        if len(self.heap) >= 2:
            maximums = self.heap[1:3]
            index = maximums.index(max(maximums)) + 1
            self.heap[index], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[index]
            maximum = self.heap.pop(len(self.heap)-1)
            self.push_down(index)
            return maximum
        elif len(self.heap) == 1:
            return self.heap.pop(0)
        else:
            raise ValueError('heap is empty')

    def build_binary_min_max_heap(self, alist):
        self.heap = alist
        for index in range((len(alist)//2)-1, -1, -1):
            self.push_down(index)

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

class DEPQ:

    def __init__(self, alist):
        self.queue = Binary_Min_Max_Heap(alist)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.queue)

    def get_min(self):
        return self.queue.find_min()

    def get_max(self):
        return self.queue.find_max()

    def put(self, i):
        self.queue.insert(i)
        return i

    def remove_min(self):
        return self.queue.remove_min()

    def remove_max(self):
        return self.queue.remove_max()

    def __str__(self):
        return self.queue.__str__()

def main():
    import inspect
    import random

    print("*" * 30 + "\nPrinting main() source code:\n" + "*" * 30)
    print(str(inspect.getsource(main)))
    print("*" * 30 + "\nPrinting main() source output:\n" + "*" * 30)

    print("This program implements a double-ended priority queue class using a min-max heap.")
    max_range = int(input("Enter max range: "))
    list_size = int(input("Enter list size: "))

    my_list = [random.randrange(1, max_range+1, 1) for i in range(list_size)]
    print("Original List:", my_list)

    my_depq = DEPQ(my_list)
    print("DEPQ min-max heap:", my_depq)

    print("size() = ", my_depq.size())
    print("is_empty() = ", my_depq.is_empty())
    print("remove_min() = ", my_depq.remove_min())
    print("DEPQ min-max heap:", my_depq)
    print("remove_max() = ", my_depq.remove_max())
    print("DEPQ min-max heap:", my_depq)
    print("remove_min() = ", my_depq.remove_min())
    print("DEPQ min-max heap:", my_depq)
    print("remove_max() = ", my_depq.remove_max())
    print("DEPQ min-max heap:", my_depq)
    print("put(max_range) = ", my_depq.put(max_range))
    print("DEPQ min-max heap:", my_depq)
    print("get_min() = ", my_depq.get_min())
    print("get_max() = ", my_depq.get_max())
    print("DEPQ min-max heap:", my_depq)   
    
if __name__ == "__main__":
    main()
