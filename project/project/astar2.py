def a_star(graph, start, goal, heuristic):
    open_set = {start}
    came_from = {}

    g_score = {vertex: float('infinity') for vertex in graph}
    g_score[start] = 0

    f_score = {vertex: float('infinity') for vertex in graph}
    f_score[start] = heuristic[start]

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])

        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.remove(current)

        for neighbor, weight in graph[current].items():
            tentative_g_score = g_score[current] + weight

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                open_set.add(neighbor)

    return []

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

# Пример использования
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

print(a_star(graph, 'A', 'D', heuristic))

