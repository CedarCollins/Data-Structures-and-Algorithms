class Queue:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

class Vertex:
    
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        self.distance = 0
        self.previous = None
        self.color = 'white'

    def get_neighbor(self, other):
        return self.neighbors.get(other, None)

    def set_neighbor(self, other, weight=0):
        self.neighbors[other] = weight

    def __repr__(self):
        return f"Vertex({self.key})"

    def __str__(self):
        return (
            str(self.key)
            + " connected to: "
            + str([x.key for x in self.neighbors])
        )

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_key(self):
        return self.key

    def get_color(self):
        return self.color

    def get_previous(self):
        return self.previous

    def get_distance(self):
        return self.distance

class Graph:
    
    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vertices.get(key, None)

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_vert, to_vert, weight=0):
        if from_vert not in self.vertices:
            self.set_vertex(from_vert)
        if to_vert not in self.vertices:
            self.set_vertex(to_vert)
        self.vertices[from_vert].set_neighbor(self.vertices[to_vert], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

def bfs(start):
    start.distance = 0
    start.previous = None
    vert_queue = Queue()
    vert_queue.enqueue(start)
    while vert_queue.size() > 0:
        current = vert_queue.dequeue()
        for neighbor in current.get_neighbors():
            if neighbor.color == "white":
                neighbor.color = "gray"
                neighbor.distance = current.distance + 1
                neighbor.previous = current
                vert_queue.enqueue(neighbor)
        current.color = "black"

def traverse(starting_vertex):
    traverse_list = []
    current = starting_vertex
    while current:
        traverse_list.insert(0, current.key)
        current = current.previous
    return(tuple(traverse_list))

def create_graph():
    buckets = {}
    graph = Graph()
    for num in range(512):
        for box in range(1,10):
            graph.add_edge(num, flip_board(num, box))
    return graph

def flip_board(node, box):
    bin_node = bin(node)[2:].rjust(9, '0')
    moves_list = [None, [5,7,8], [4,6,7,8], [3,6,7], [2,4,5,8], [1,3,4,5,7],
                 [0,3,4,6], [1,2,5], [0,1,2,4], [0,1,3]]
    if box >= 1 and box <= 9:
        return flip_bits(bin_node, moves_list[box])
    else:
        raise ValueError('invalid box number')

def flip_bits(bin_node, bit_indeces):
    for index in bit_indeces:
        if bin_node[index] == '0':
            bin_node = bin_node[:index] + '1' + bin_node[index+1:]
        else:
            bin_node = bin_node[:index] + '0' + bin_node[index+1:]
    return int(bin_node, 2)

def find_move(start, end):
    bin_start = bin(start)[2:].rjust(9, '0')
    bin_end = bin(end)[2:].rjust(9, '0')
    bits_dict = {(5,7,8): 1, (4,6,7,8): 2, (3,6,7): 3, (2,4,5,8): 4, (1,3,4,5,7): 5,
                 (0,3,4,6): 6, (1,2,5): 7, (0,1,2,4): 8, (0,1,3): 9}
    changed_bits = find_changed_bits(bin_start, bin_end)
    if changed_bits in bits_dict:
        return bits_dict[changed_bits]
    else:
        raise ValueError(f'{start} and {end} are not neighboring nodes')
    
def find_changed_bits(bin_start, bin_end):
    index_list = []
    for index in range(9):
        if bin_start[index] != bin_end[index]:
            index_list.append(index)
    return tuple(index_list)

def coin_layout(node):
    bin_node = bin(node)[2:].rjust(9, '0')
    string = ''
    for bit in bin_node:
        if bit == '0':
            string += 'H'
        else:
            string += 'T'
    return string[6:][::-1] + '\n' + string[3:6][::-1] + '\n' + string[:3][::-1] + '\n'

def main():
    graph = create_graph()
    node = 0

    print('Welcome to Flipper!' + '\n' * 2 +
          'You begin with nine coins, showing "heads", arranged in a 3x3 grid:' + '\n' * 2 +
          'HHH    123\n' +
          'HHH    456  <= Coin Choice Options 1-9\n' +
          'HHH    789' + '\n' * 2 +
          'Choose a coin to flip it over, along with those vertically and\n' +
          'horizontally adjacent.' + '\n' * 2 +
          'The object of the game is to end up with all coins showing "tails".' + '\n' *2 +
          'If you are stuck, choose Option 0 to show the solution.  :)' + '\n'*2)
    
    print(coin_layout(node))

    isSolved = False
    while not isSolved:
        vertex_list = []
        for neighbor in graph.get_vertex(node).get_neighbors():
            vertex_list.append(neighbor.get_key())
            
        print('Option 0: Solve; Options 1-9: Choose Node\n' +
              f'Node {node} (' + bin(node)[2:].rjust(9, '0') + ')\n' +
              f'Node {node} connected To: ' + str(sorted(vertex_list)) + '\n')
        
        try:
            box = int(input('Choose Option 0-9: '))
        except ValueError:
            print('\nInvalid option. Please try again.\n\n' + coin_layout(node))
            continue
                    
        if box == 0:
            bfs(graph.get_vertex(node))
            traverse_tuple = traverse(graph.get_vertex(511))
            print('\n' + coin_layout(node))
            previous_node = node
            
            for current_node in traverse_tuple[1:]:
                print(f'Computer Chooses Option {find_move(previous_node, current_node)}: ')
                print('\n' + coin_layout(current_node))
                previous_node = current_node

            isSolved = True
        elif box >= 1 and box <= 9:
            node = flip_board(node, box)
            print('\n' + coin_layout(node))
        else:
            print('\nInvalid option. Please try again.\n\n' + coin_layout(node))

        if node == 511:
            isSolved = True

    print('Success!  :)')

if __name__ == '__main__':
    main()
