### Основные этапы:

1. **Определение целевой функции**:
   - Это функция, которую нужно минимизировать, принимающая два аргумента (x1, x2):
     ```python
     def objective_function(x1, x2):
         return 500 * x1 + 200 * x2
     ```
   Здесь \( 500x1 + 200x2 \) — это целевая функция.

2. **Проверка ограничений**:
   - В следующей части кода задана функция для проверки, удовлетворяют ли точки ограничениям:
     ```python
     def check_constraints(x1, x2):
         return (x1 + x2 <= 100 and 2*x1 + x2 >= 50 and x1 >= 0 and x2 >= 0)
     ```
   Это означает, что возможные решения должны удовлетворять следующим условиям:
   - \( x1 + x2 \leq 100 \)
   - \( 2x1 + x2 \geq 50 \)
   - \( x1 \geq 0 \)
   - \( x2 \geq 0 \)

3. **Нахождение пересечений ограничений**:
   - Функция `solve_intersection` решает системы линейных уравнений, чтобы найти точки пересечения между прямыми, заданными ограничениями:
     ```python
     def solve_intersection(a1, b1, c1, a2, b2, c2):
         # Решение системы уравнений вида a1*x + b1*y = c1 и a2*x + b2*y = c2
         determinant = a1 * b2 - a2 * b1
         if determinant == 0:
             return None  # Прямые параллельны
         else:
             x = (c1 * b2 - c2 * b1) / determinant
             y = (a1 * c2 - a2 * c1) / determinant
             return (x, y)
     ```
   Это находит точку пересечения двух прямых, если они не параллельны.

4. **Поиск всех допустимых точек**:
   - Программа проходит по всем комбинациям ограничений, решает систему уравнений для каждой пары, а затем проверяет, удовлетворяет ли найденная точка всем ограничениям.
   - Все допустимые точки сохраняются в список `points`.

5. **Вычисление значений целевой функции**:
   - Программа проверяет каждую допустимую точку, вычисляет значение целевой функции для каждой из них, и затем находит минимальное значение:
     ```python
     min_value = float('inf')
     min_point = None
     for (x1, x2) in points:
         value = objective_function(x1, x2)
         if value < min_value:
             min_value = value
             min_point = (x1, x2)
     print(f"Минимальное значение целевой функции: {min_value} в точке {min_point}")
     ```

6. **Результат**:
   - Минимальное значение целевой функции было найдено: 12812 в точке (37.0, 50.0).
   - Выводятся также все значения и соответствующие им точки:
     ```
     Все значения:
     15798.0 40.0 66.0
     12812.0 37.0 50.0
     23370.0 38.0 114.0
     19080.0 35.0 90.0
     ```

## Метод графического решения

В задачах с двумя переменными можно решать задачу ЛП графически, строя на плоскости линии ограничений и находя точку, где целевая функция достигает оптимума. Этот метод наглядно показывает, как ограничения формируют область допустимых решений и где находится оптимальная точка.
