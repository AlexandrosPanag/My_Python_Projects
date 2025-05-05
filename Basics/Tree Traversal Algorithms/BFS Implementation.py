#By Alexandros Panagiotakopoulos - alexandrospanag.github.io

from collections import deque

def bfs(start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

def get_neighbors(num):
    return [num+1, num-1, num*2, num//2]

start = 1
end = 20
path = bfs(start, end)
if path:
    print(f"Shortest path from {start} to {end}: {path}")
else:
    print(f"No path found from {start} to {end}")
