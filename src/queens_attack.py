def queens_attack(n, k, r_q, c_q, obstacles):
    obstacles = set((i, j) for i, j in obstacles)
    count = 0
    directions = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if not (i == 0 and j == 0)]
    print(directions)
    for dr, dc in directions:
        r_pos = r_q + dr
        c_pos = c_q + dc
        while (
            (r_pos, c_pos) not in obstacles
            and r_pos > 0
            and r_pos < n + 1
            and c_pos > 0
            and c_pos < n + 1
        ):
            count += 1
            r_pos += dr
            c_pos += dc

    return count
