# Depth First Search (DFS)
A recursive algorithm to search all vertices of a graph by visiting all adjacent nodes before going to the next node.

# Algorithm 
1. Put any of the graph's vertices at the back of a queue.
2. Take the front item of the queue and add it to the visited list.
3. Add all of the vertex's adjacent nodes that aren't visited to the back of the queue.
4. Repeat Steps 2 and 3.

## Example
Let's say we have the following graph:
```
# Note that the nodes are connected by |, |, or -

O - 3
| \ 
1 - 2 - 4

# Visited: []
# Queue: []
```

We start at 0. `+` means visited. We add all adjacent vertices of 0 (1, 2, 3) to the queue.
```
+ - 3
| \ 
1 - 2 - 4

# Visited: [0]
# Queue: [1, 2, 3]
```

We add 1 to the visit list now because it's front of the queue. There are no adjacent vertexes for Node 1 that aren't in the queue so now we visit 2. 
```
+ - 3
| \ 
+ - 2 - 4

# Visited: [0, 1]
# Queue: [2, 3]
```

Vertex 2 has an adjacent node that has not been visited or is in the queue. So we add it to the queue.
```
+ - 3
| \ 
+ - + - 4

# Visited: [0, 1, 2]
# Queue: [3, 4]
```

We visit 3 next since it's first in the queue. All adjacent nodes are already visited or in queue.
```
+ - +
| \ 
+ - + - 4

# Visited: [0, 1, 2, 3]
# Queue: [4]
```

Next we visit 4. 4 has no adjacent nodes that are unvisited. The queue is now empty so we have completed BFS.

```
+ - +
| \ 
+ - + - 4

# Visited: [0, 1, 2, 3, 4]
# Queue: []
```

# Code
```
import collections

def bfs(graph, node):
    visited, queue = set(), collections.deque([node])
    visited.add(node)

    while queue:
        vertex = queue.popleft()
        print(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    graph = {'0': set(['1', '2']),
            '1': set(['0', '3', '4']),
            '2': set(['0']),
            '3': set(['1']),
            '4': set(['2', '3'])}
    
    print(bfs(graph, '0'))

main()
```

# Analysis
V is the number of nodes 
E is the number of edges

**Time Complexity:** O(V + E) 
**Space Complexity:** O(V)

# Application
1. Build index by search index.
2. GPS navigation
3. Path finding algorithms
4. Cycle dtection in unidirected graph

# Resource 
https://www.programiz.com/dsa/graph-bfs