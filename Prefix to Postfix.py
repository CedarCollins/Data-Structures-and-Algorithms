"""
This program converts algebraic expressions in prefix form
(like + + A * B C D) into postfix form (A B C * + D +)

Here are some other example prefix expressions:

* + A B + C D

+ * A B * C D

+ + + A B C D
"""

class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)

    def __str__(self):
        return str(self._items)

def prefix_to_postfix(pre_str):
    operand_stack = Stack()
    pre_list = pre_str.split()
    post_list = []
    string = ''

    for token in pre_list:
        if token in '+-*/^':
            operand_stack.push(token)
            string += 'o'
        else:
            post_list.append(token)
            string += 'v'
        while 'ovv' in string:
            string = string.replace('ovv', 'v', 1)
            post_list.append(operand_stack.pop())

    while not operand_stack.is_empty():
        post_list.append(operand_stack.pop())

    return " ".join(post_list)
    
def main():
    prefix = input("Enter Prefix Expression: ")
    postfix = prefix_to_postfix(prefix)
    print("Converted to Postfix is: " + postfix)

if __name__ == "__main__":
    main()
