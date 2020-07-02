from collections import deque


class Graph:
    def __init__(self, num_node):
        self.neighbours = {i: set() for i in range(num_node)}

    def connect(self, source, dest):
        self.neighbours[source].add(dest)
        self.neighbours[dest].add(source)

    def find_all_distances(self, source):
        distances = [-1] * len(self.neighbours)
        distances[source] = 0

        queue = deque([source])
        while len(queue) > 0:
            current = queue.popleft()
            for node in self.neighbours[current]:
                if distances[node] == -1:
                    distances[node] = distances[current] + 6
                    queue.append(node)

        distances.pop(source)
        return distances
