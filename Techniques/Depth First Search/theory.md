# Depth First Search (DFS)
A recursive algorithm to search all vertices of a graph by going far as possible and then backtracking when you encounter all nodes that are visited.

# Algorithm 
1. Put any of the vertices on top of a stack.
2. Take the top item of the stack and add it to visited.
3. Create a list of that vertex's adjacent nodes. Add the any adjacent nodes that aren't in visited to the top of the stack (if they don't already exist).
4. Repeat Steps 2 and 3 until the stack is empty. 

## Example
Let's say we have the following graph:
```
# Note that the nodes are connected by |, |, or -
O - 3
| \ 
1 - 2 - 4

# Visited: []
# Stack: []
```

Let's say we start at vertex one. Let's put it in the visited list. Put all adjacent vertices in a stack. A `+` symbol has been put for nodes we visited.
```
+ - 3
| \ 
1 - 2 - 4

# Visited: [0]
# Stack: [1, 2, 3]
```

Next, visit the first node on top of the stack which is 1. 
```
+ - 3
| \ 
+ - 2 - 4

# Visited: [0, 1]
# Stack: [2, 3]
```

There are two adjacent nodes: 0 and 2. 0 already has been visited so we visit 2 (it's already on top of the stack).
```
+ - 3
| \ 
+ - + - 4

# Visited: [0, 1, 2]
# Stack: [3]
```

Vertex 2 has the following adjacent nodes: 0, 1, 4. 4 has not been visited so we add it on top of the stack and visit it. 

```
+ - 3
| \ 
+ - + - +

# Visited: [0, 1, 2]
# Stack: [4, 3]
```

```
+ - 3
| \ 
+ - + - +

# Visited: [0, 1, 2, 4]
# Stack: [3]
```

Vertex four has adjacent nodes 1 and 2 but they're already visited. So we backtracked to 2 and 1. Once we hit 0, there's an adjacent node (3) that hasn't been visited (it's also on top of the stack) so we visit it.
```
+ - 3
| \ 
+ - + - +

# Visited: [0, 1, 2, 4, 3]
# Stack: []
```
# Code
```
def dfs(graph, node, visited=None): 
    # if the `visited` param is `None`, then create a new set
    if visited is None:
        visited = set()

    # add the node being passed in 
    visited.add(node)

    """
    graph[node] - visited is set difference. So if graph[node] == {1, 2, 3} and visited = {1, 4, 5}. 
    Then the result would be {2, 3}

    See: https://www.geeksforgeeks.org/python-set-difference/
    """
    for next in graph[node] - visited: 
        dfs(graph, next, visited)
    return visited 

def main():
    graph = {'0': set(['1', '2']),
            '1': set(['0', '3', '4']),
            '2': set(['0']),
            '3': set(['1']),
            '4': set(['2', '3'])}
    
    print(dfs(graph, '0'))

main()
```

# Analysis
V is the number of nodes 
E is the number of edges

**Time Complexity:** O(V + E) 
**Space Complexity:** O(V)

# Application
1. Find path
2. Test if graph is bipartite
3. Find strongly connected components of a graph
4. Detect cycles in a graph.

# Resource 
https://www.programiz.com/dsa/graph-dfs