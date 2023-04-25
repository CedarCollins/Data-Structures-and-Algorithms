"""
This program sorts a list of random numbers one digit at a time
(from the one's digit and up) such that the final output is a
sorted list. It uses a number of queues, with one for each digit and
an additional main queue, to keep the numbers in order as each progressive
digit is sorted.
"""

import random

class Queue():
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def peek(self):
        return self._items[0]
    
def radix_sort(max_range, list_len):
    len_max = len(str(max_range))
    bin_main = Queue()
    digit_queues = []

    #create main queue
    for i in range(list_len):
        rand_num = (random.randint(1, max_range))
        bin_main.enqueue(rand_num)

    #create queues for each digit
    for i in range(10):
        digit_queues.append(Queue())

    #loop for each line of radix sort
    for x in range(len_max + 1):
        print_list = []
        
        while not bin_main.is_empty():
            
            num = bin_main.dequeue()
            if x > len(str(num)):
                digit_queues[0].enqueue(num)
            else:
                digit = int((num % 10**x) // 10**(x-1))
                digit_queues[digit].enqueue(num)

        for bin_name in range(10)[::-1]:
            while not digit_queues[bin_name].is_empty():
                bin_main.enqueue(digit_queues[bin_name].dequeue())
                print_list.append(bin_main.peek())

        #prints each line
        print_list.reverse()
        print('Radix Pass ' + f'{x}:'.rjust(len_max//10 + 2), end='')
        for item in print_list:
            print(str(item).rjust(len_max + 1), end='')
        print('')
                            
def main():
    max_range = int(input('Enter max range: '))
    list_len = int(input('Enter list size: '))
    
    radix_sort(max_range, list_len)

if __name__ == '__main__':
    main()
