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

def postfix_to_prefix(post_str):
    variable_stack = Stack()
    operand_stack = Stack()
    post_list = reversed(post_str.split())
    pre_list = []
    string = ''

    for token in post_list:
        if token in '+-*/^':
            operand_stack.push(token)
            string += 'o'
        else:
            pre_list.insert(0, token)
            string += 'v'
        while 'ovv' in string:
            string = string.replace('ovv', 'v', 1)
            pre_list.insert(0, operand_stack.pop())

    while not operand_stack.is_empty():
        pre_list.insert(0, operand_stack.pop())

    return ' '.join(pre_list)

def main():
    postfix = input('Enter Postfix Expression: ')
    prefix = postfix_to_prefix(postfix)
    print('Converted to Prefix is: ' + prefix)

if __name__ == "__main__":
    main()
