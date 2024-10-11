import heapq 

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start], priority_queue = 0, [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue 

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight 

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor)) 

    return distances 

def main():
    # Пример использования:
    graph = {
        'Aksay': {'Birminghem': 4, 'Cambridge': 7},
        'Birminghem': {'Aksay': 4, 'Dover': 2, 'Edinburgh': 8},
        'Cambridge': {'Aksay': 7, 'Dover': 2, 'Edinburgh': 5},
        'Dover': {'Birminghem': 2, 'Cambridge': 2, 'Edinburgh': 1,'Folkestone': 4},
        'Edinburgh': {'Cambridge': 5, 'Dover': 1, 'Folkestone': 11},
        'Folkestone': {'Birminghem': 8, 'Dover': 4, 'Edinburgh': 11}
    }

    result = dijkstra(graph, 'Aksay')
    print("Кратчайшие расстояния до городов: ")
    for vertex, distance in result.items():
        print(f"До города {vertex}: {distance}")

if __name__ == "__main__":
    main()
