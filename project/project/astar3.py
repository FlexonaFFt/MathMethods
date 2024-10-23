import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # Позиция узла (x, y)
        self.parent = parent  # Родительский узел
        self.g = 0  # Стоимость от начальной точки до текущего узла
        self.h = 0  # Оценочная стоимость от текущего узла до конечного
        self.f = 0  # Общая стоимость: f = g + h

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node_position, end_position):
    """Функция для вычисления эвристики. Используем манхэттенское расстояние."""
    return abs(node_position[0] - end_position[0]) + abs(node_position[1] - end_position[1])

def astar(grid, start, end):
    """Алгоритм A* для поиска кратчайшего пути."""
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    closed_list = []

    heapq.heappush(open_list, start_node)

    n = len(grid)  # Количество строк в сетке

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Возвращаем путь в обратном порядке

        # Проверяем соседей (влево, вправо, вверх, вниз)
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for neighbor_position in neighbors:
            neighbor_pos = (current_node.position[0] + neighbor_position[0],
                            current_node.position[1] + neighbor_position[1])

            # Преобразуем координаты декартовой системы в индексы сетки
            grid_y = n - neighbor_pos[1] - 1
            grid_x = neighbor_pos[0]

            # Проверяем, что сосед в пределах сетки и не является препятствием
            if grid_x < 0 or grid_x >= len(grid[0]) or \
               grid_y < 0 or grid_y >= len(grid) or \
               grid[grid_y][grid_x] == 1:
                continue

            neighbor_node = Node(neighbor_pos, current_node)

            if neighbor_node in closed_list:
                continue

            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_node.position, end_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if any(open_node for open_node in open_list if neighbor_node == open_node and neighbor_node.g > open_node.g):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None  # Если пути не существует

# Пример использования: сетка на классической декартовой системе координат
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Декартовые координаты (x, y)
end = (3, 1)    # Декартовые координаты (x, y)

path = astar(grid, start, end)
print("Путь:", path)

