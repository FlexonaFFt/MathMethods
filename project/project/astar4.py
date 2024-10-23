import heapq

# Функция для вычисления манхэттенского расстояния между двумя точками
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def astar(grid, start, goal):
    cost = {start: 0}
    came_from = {start: None}
    priority_queue = [(0, start)]

    n = len(grid)      
    m = len(grid[0])  

    while priority_queue:
        current_cost, current_point = heapq.heappop(priority_queue)

        if current_point == goal:
            break

        for neighbor in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current_point[0] + neighbor[0], current_point[1] + neighbor[1]
            grid_x = x
            grid_y = n - y - 1  
        
            if 0 <= grid_x < m and 0 <= grid_y < n and grid[grid_y][grid_x] == 0:
                new_cost = cost[current_point] + 1
                if (x, y) not in cost or new_cost < cost[(x, y)]:
                    cost[(x, y)] = new_cost
                    priority = new_cost + manhattan_distance((x, y), goal)
                    heapq.heappush(priority_queue, (priority, (x, y)))
                    came_from[(x, y)] = current_point

    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def main():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (3, 3)  
    result_path = astar(grid, start, goal)

    print("Путь от A до B:")
    for point in result_path:
        print(point)

if __name__ == '__main__':
    main()

