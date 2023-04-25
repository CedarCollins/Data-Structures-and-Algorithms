"""
This program uses dynamic programming to find the total number of
character insertions, deletions, or substitutions needed to transform
one string of any length to another string of any length.
"""

def store(string1, string2):
    
    dictionary = {}

    print('\n' + ' '*8 + '  '.join([*string2]))
    for y in range(len(string1) + 1):
        print_list = []
        if y == 0:
            print_list.append(' ')
        else:
            print_list.append(string1[:y][-1])
        for x in range(len(string2) + 1):
            if len(string1[:y]) == 0:
                dictionary[(x, y)] = x
            elif len(string2[:x]) == 0:
                dictionary[(x, y)] = y
            elif string1[:y][-1] == string2[:x][-1]:
                dictionary[(x, y)] = dictionary[(x - 1, y - 1)]
            else:
                dictionary[(x, y)] = 1 + min(dictionary[(x - 1, y - 1)],
                                               dictionary[(x, y - 1)],
                                               dictionary[(x - 1, y)])
            print_list.append(str(dictionary[(x, y)]).rjust(3))
        print('  ' + ''.join(print_list))

    print('\n' + f'store("{string1}", "{string2}") = {dictionary[(len(string2), len(string1))]}')
        
def main():
    
    print(
"""
This program efficiently computes the minimum total number of character 
insertion, deletion, and/or substitution operations required to transform 
one string into another.

The String Transformation Operations REquired (STORE) function can be 
defined recursively via the following pseudocode:

if len(string1) == 0:                      # base case: string1 empty
    store(string1, string2) = len(string2) # this many insertions to string 1 required
elif len(string2) == 0:                    # base case: string2 empty
    store(string1, string2) = len(string1) # this many deletions from string 1 required
elif string1[-1] == string2[-1]:           # last characters are the same
    store(string1, string2) = store(string1[0:-1], string2[0:-1]) # no operation needed
else:                                      # last characters differ
    store(string1, string2) = 1+min(store(string1[0:-1], string2      ), # insertion
                                    store(string1      , string2[0:-1]), # deletion
                                    store(string1[0:-1], string2[0:-1])) # substitution

Rather than computing overlapping subproblem answers repeatedly, this program 
computes each of them once, storing them into a table (dynamic programming).
""")

    string1 = input('Enter string1: ')
    string2 = input('Enter string2: ')

    store(string1, string2)

if __name__ == '__main__':
    main()
