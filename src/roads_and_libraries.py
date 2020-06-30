def roads_and_libraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib

    neighbours = {i: set() for i in range(n)}
    visited = [False] * n
    connected_components = 0

    def dfs(origin):
        if visited[origin]:
            return

        visited[origin] = True
        for city in neighbours[origin]:
            dfs(city)

    for origin, destination in cities:
        origin = origin - 1
        destination = destination - 1
        neighbours[origin].add(destination)
        neighbours[destination].add(origin)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            connected_components += 1

    total_cost = connected_components * c_lib + (n - connected_components) * c_road
    return total_cost


def roads_and_libraries_ds(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib

    item_set_id = {i: i for i in range(n)}
    disjoint_sets = {i: {i} for i in range(n)}

    for origin, destination in cities:
        origin = origin - 1
        destination = destination - 1

        if item_set_id[origin] != item_set_id[destination]:
            temp = item_set_id[destination]
            for i in disjoint_sets[temp]:
                item_set_id[i] = item_set_id[origin]
                disjoint_sets[item_set_id[origin]].add(i)
            del disjoint_sets[temp]

    total_cost = len(disjoint_sets) * c_lib + (n - len(disjoint_sets)) * c_road

    return total_cost
