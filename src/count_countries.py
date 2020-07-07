def count_countries(matrix):
    if len(matrix) == 0:
        return 0

    r, c = len(matrix), len(matrix[0])
    visited = [[False] * c for _ in range(r)]

    def dfs(i, j):
        if i < 0 or i >= r or j < 0 or j >= c or matrix[i][j] != "1" or visited[i][j]:
            return
        visited[i][j] = True
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == "1" and not visited[i][j]:
                count += 1
                dfs(i, j)
    return count
