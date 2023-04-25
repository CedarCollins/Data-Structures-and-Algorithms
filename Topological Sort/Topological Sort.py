"""
This program uses depth first search in a graph to make a topological sort
of the data within the graph. The example file given is to create a sort
for prerequisites for classes required for a computer science degree.

Format your own file like this:
[An item]: [All prerequisites for that item]
...
"""

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
        self.discovery_time = 0
        self.closing_time = 0

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

    def get_discovery_time(self):
        return self.discovery_time

    def get_closing_time(self):
        return self.closing_time

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

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.color = "white"
            vertex.previous = -1
        for vertex in self:
            if vertex.color == "white":
                self.dfs_visit(vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.color = "gray"
        self.time = self.time + 1
        start_vertex.discovery_time = self.time
        for next_vertex in start_vertex.get_neighbors():
            if next_vertex.color == "white":
                next_vertex.previous = start_vertex
                self.dfs_visit(next_vertex)
        start_vertex.color = "black"
        self.time = self.time + 1
        start_vertex.closing_time = self.time

def create_graph(file_name):
    prereq_dict = {}
    infile = open(file_name,"r")

    #put data from file into a dictionary
    for line in infile:
        print(f'Processing input file line->{line}', end = '')
        line_split = line.split(":")
        if len(line_split[1].strip()) > 0:
            prereq_dict[line_split[0]] = line_split[1].split()
        else:
            prereq_dict[line_split[0]] = None
            
    infile.close()

    #put data from dictionary into graph
    graph = DFSGraph()
    for key in prereq_dict:
        if key not in graph:
            graph.set_vertex(key)
        if prereq_dict[key]:
            for item in prereq_dict[key]:
                graph.add_edge(item, key)

    return graph

def topological_sort(graph):
    print('Performing topological sort...')
    graph.dfs()
    vert_dict = {}
    vert_closings = []
    ordered_verts = []
    for vertex in graph:
        vert_closings.append(vertex.closing_time)
        vert_dict[vertex.closing_time] = vertex.get_key()
    for closing_time in sorted(vert_closings, reverse = True):
        ordered_verts.append(vert_dict[closing_time])
    print('Ordered list:\n' + str(ordered_verts))
    
def main():
    infile = "prereq.txt"
    print('This program reads in a list of courses and prerequisites, and determines\n' +
          'a valid ordering subject to prerequisite constraints via topological sort.\n' +
          f'Reading input file "{infile}"...')
    graph = create_graph(infile)
    topological_sort(graph)

if __name__ == '__main__':
    main()
