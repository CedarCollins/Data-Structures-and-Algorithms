"""
This program sorts the words in a string one letter at a time
(from the right most letter and up) such that the final output is an
alphabetical sort of the words in the string. It uses a number of queues,
with one for each digit and an additional main queue, to keep the numbers
in order as each progressive digit is sorted.

Input is in the format of "{word1} {word2} ... {wordN}"
"""

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

def radix_sort(word_str):

    unspaced_word_list = word_str.split()
    maxlen = max(len(word) for word in unspaced_word_list)
    word_list = []
    
    for i in range(len(unspaced_word_list)):
        word = unspaced_word_list[i]
        word_list.append(word + ' '*(maxlen-len(word)))
    
    bin_main = Queue()
    for item in word_list[::-1]:
        bin_main.enqueue(item)
    
    letters = ' abcdefghijklmnopqrstuvwxyz'
    letter_queues = []
    #letter_queue[1...26] is for a...z
    #letter_queue[0] is for ' '
    for i in range(27):
        letter_queues.append(Queue())

    for x in range(maxlen + 1):
        print_list = []

        while not bin_main.is_empty():
            word = bin_main.dequeue()
            if x == 0 or word[maxlen - x] == ' ':
                letter_queues[0].enqueue(word)
            else:
                letter_queues[letters.index(word[maxlen - x])].enqueue(word)

        for bin_num in range(27)[::-1]:
            while not letter_queues[bin_num].is_empty():
                bin_main.enqueue(letter_queues[bin_num].dequeue())
                print_list.insert(0, bin_main.peek())

        print('Radix Pass ' + f'{x}:'.rjust(maxlen//10 + 2), ' '.join(print_list))
    
def main():
    word_str = input('Enter word list: ')
    print('')
    radix_sort(word_str)

if __name__ == '__main__':
    main()
