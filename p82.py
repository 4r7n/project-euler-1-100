with open("p81_matrix.txt", "r") as f:
    M = [list(map(int, s.split(","))) for s in f.read().split("\n")[:-1]]


#M = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 50], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]



import heapq
from math import inf

def astar(grid, start):
    n, m = len(grid), len(grid[0])

    c_min = min(min(row) for row in grid)

    def h(x, y):
        return (m - 1 - y) * c_min

    pq = []
    heapq.heappush(pq, (h(*start), 0, start))

    g_score = {start: 0}
    parent = {}

    directions = [(1,0), (-1,0), (0,1)]  # up, down, right

    while pq:
        f, g, (x, y) = heapq.heappop(pq)

        # goal: ANY cell in right column
        if y == m - 1:
            path = [grid[x][y]]
            while (x, y) in parent:
                x, y = parent[(x, y)]
                path.append(grid[x][y])
            return sum(path[::-1])

        if g != g_score.get((x, y), inf):
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            new_g = g + grid[nx][ny]

            if new_g < g_score.get((nx, ny), inf):
                g_score[(nx, ny)] = new_g
                parent[(nx, ny)] = (x, y)

                heapq.heappush(
                    pq,
                    (new_g + h(nx, ny), new_g, (nx, ny))
                )

    return None

print(min(astar(M, (i, 0)) for i, it in enumerate(M)))