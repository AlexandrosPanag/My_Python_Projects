#By Alexandros Panagiotakopoulos - alexandrospanag.github.io

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited

graph = {
    1: set([2, 3]),
    2: set([1, 4, 5]),
    3: set([1, 6, 7]),
    4: set([2]),
    5: set([2, 8]),
    6: set([3]),
    7: set([3]),
    8: set([5])
}

print(dfs(graph, 1))

