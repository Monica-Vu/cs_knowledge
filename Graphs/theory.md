# Graphs
* A non-linear data structure that has a finite set of node (vertices) that are connected by edges. 
* Edges can be directed or undirected along with an optional value (this is known as a weighted graph). 

## Trees
Unidirected non-cyclic graph in which any two vertices are connected by exactly on edge 

## Uses
* Model relationship
* Represent networks (real-life or social)
* Paths in a city of telephone network 

## Representations 
In algorithm interview, you are typically given the input as 2D matrices where the cells are the nodes and each cell can traverse to its adjacent cells. Being able to traverse through a 2D matrix is important. Make sure to do boundary checking. 

### Adjacency matrix
* A 2D list/array of size V x V, where V is the number of vertices or nodes in the graph
* 1 means there's a edge from vertex i to j while 0 means there's no connection 
* Represents undirected graphs
* Can be used to represent weighted graphs 

```
0 1 2 3 4
0 0 1 0 0
1 0 0 1 1
2 0 0 1 0
3 0 1 0 0
4 0 1 0 0
```

#### Advantages
* Easier to implement and follow than adjaceny list
* Identifying if there's an edge from a vertex u to v only takes O(1) 
* Removing an edge only takes O(1) -- only need to change to 0

#### Disadvantages
* Consumes more space than necessary (OV^2) regardless of size
* Adding a vertex takes O(V^2) 

### Adjacency List
* Use a list to represent other nodes it is connected to (or it has vertices to)
    * You might see weights associated with them 
```
0: [1, 4]
1: [0, 4, 2, 3]
2: [1, 3]
4: [3, 0, 1]
```

#### Advantages
* Saves space: only uses O(|V| + |E|) but worst case is O(V^2)
* can easily find all vertices adjacent to a vertex 

#### Disadvantages
* Certain queries (checking if an edge from another vertex can cost O(v))

#### Implementation 
```
class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None
```

```
from [file_name] import AdjNode 

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
    
    # assumption: undirected graph (otherwise, you can remove the last three lines of the function)
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = None

    def print_graph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]

            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
```
 
### Hashmap of hashmaps (dictionary of dictionary)
```
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, s, d):
        if s not in verties.keys():
            self.vertices[s] = set(d)
        else:
            self.vertices[s].add(d)
```

```
class Graph:
    def __init__(self):
        self.vertices = defaultdict(list)

    def add_edge(self, s, d):
        self.vertices[s].append[d]
```

## Algorithms
### Breadth-first Search
* Starting at the root node, visit all neighbours or level before proceeding to the next
* Keep a queue of nodes to visit next (i.e same level) and then visit all the neighbours of nodes in the queue 
* If implementing for a graph (which might have cycles), create a DTS to keep track if it's visited

#### Implementation
For the purposes of the implementation, we'll assume that it has the classes from the third representation type of Graphs.
```
def bfs(self, node):
    visited = [] 
    queue = [] 

    queue.append(node)
    visited.append(node)

    while queue:
        node = queue.pop(0)
        print(node, end = " ")

        for i in self.vertices[node]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

```
Time Complexity: O(V + E)
Space Complexity: O(V)

### Depth-first Search
* Starting at the root, pick a node to visit. Then visit that node's neighbour. If we encounter a neighbour that is already visited, we backtrack. We continue until all are visited.
* For graphs with cycles, be sure to be track if a node is visited 

#### Implementation
```
def dfs_util(self, node, visited):
    visited.add(node)
    print(v, end=' ')

    for neighbour in self.vertices[node]:
        if neighbour not in visited:
            self.dfs_util(neighbour, visited)
    
def dfs(self, node):
    visited = set()
    self.dfs_util(node, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.DFS(2)
```
* For disconnected graphs, you will have to call DFS on unreachable nodes 

Time Complexity: O(V + E)
Space Complexity: O(V)

## Common Corner Cases to Consider
* Empty Graphs
* Graphs with 1-2 nodes
* Disjoint graphs
* Graphs with cycles

# Sources
https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/
https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
https://www.techinterviewhandbook.org/algorithms/graph/