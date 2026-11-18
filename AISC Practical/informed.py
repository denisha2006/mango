

# Aim: Have exactly 2 litres in the 4 litre jug

import heapq

def hurestic(a):
    return abs(2 - a[0])

def AStar():
    GOAL = [0, 2]
    start = [0, 0]

    visited = []
    heap = []

    heapq.heappush(heap, (hurestic(start), start, []))

    while heap:
        h, [a, b], path = heapq.heappop(heap)

        if [a, b] in visited:
            continue

        visited.append([a, b])

        if [a,b] == GOAL:
            return path + [("Goal Reached", [a,b])]
        paths = [
            ([4, b], "Fill Jug A"),
            ([a, 3], "Fill Jug B"),
            ([0, b], "Empty Jug A"),
            ([a, 0], "Empty Jug B"),
            ([a-min(a, 3-b), b+min(a, 3-b)], "Pour A into B"),
            ([a+min(b, 4-a), b-min(b, 4-a)], "Pour B into A")
        ]

        for new, action in paths:
            if new in visited:
                continue
            heapq.heappush(heap, (h + hurestic(new), new, path + [(action, new)]))
path = AStar()

for step, state in path:
    print(step, "->", state)
