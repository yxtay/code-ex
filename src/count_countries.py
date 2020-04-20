def count_countries(matrix):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def explore(row, col):
        queue = [(row, col)]
        explored = set(queue)
        while queue:
            row, col = queue.pop()

            try:
                if matrix[row][col] == "1":
                    for dr, dc in directions:
                        coordinates = row + dr, col + dc
                        if coordinates not in explored:
                            explored.add(coordinates)
                            queue.append(coordinates)
            except IndexError:
                pass
        return explored

    count = 0
    explored = set()
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if (i, j) not in explored and value == "1":
                count += 1
                explored = explored.union(explore(i, j))

    return count
