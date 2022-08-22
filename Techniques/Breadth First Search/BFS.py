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