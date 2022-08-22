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