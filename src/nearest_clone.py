from collections import deque


def find_shortest(graph_nodes, graph_from, graph_to, ids, val):
    neighbours = {i + 1: set() for i in range(graph_nodes)}

    for origin, dest in zip(graph_from, graph_to):
        neighbours[origin].add(dest)
        neighbours[dest].add(origin)

    queue = deque()
    visited = {}

    for i, id in enumerate(ids):
        if id == val:
            visited[i + 1] = (i + 1, 0)
            queue.append(i + 1)

    while queue:
        current = queue.popleft()
        source, path_len = visited[current]

        for node in neighbours[current]:
            if node not in visited:
                visited[node] = (source, path_len + 1)
                queue.append(node)
            else:
                node_source, node_path_len = visited[node]
                if node_source != source:
                    return path_len + node_path_len + 1
    return -1
