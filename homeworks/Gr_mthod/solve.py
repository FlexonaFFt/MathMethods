import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from itertools import combinations

# Усовершенствуем график на основе структуры исходного кода
class LinearForm2D:
    def __init__(self, a, b, c=None, sign=None):
        self.a = a
        self.b = b
        self.c = c
        self.sign = sign
        self.label = ((str(a) if a != 1 else '') + " x_1 " if a != 0 else '') + \
                     ("+" + (str(b) if b != 1 else '') + " x_2 " if b != 0 else '') + \
                     "=" + str(c)

    # Выразить x_2 через x_1:
    def y_func(self, x):
        return (self.c - self.a * x) / self.b if self.b and self.b != 0.0 else None

    # Выразить x_1 через x_2:
    def x_func(self, y):
        return (self.c - self.b * y) / self.a if self.a and self.a != 0.0 else None

    # Подготовить график:
    def prepare_plot(self, s=0, f=100, num=10, color='black'):
        ps = np.linspace(s, f, num)
        xs = self.x_func(ps)
        if xs is not None:
            plt.plot(xs, ps, label=self.label, color=color)
        else:
            ys = self.y_func(ps)
            if ys is not None:
                plt.plot(ps, ys, label=self.label, color=color)
        plt.legend()

    def f_value(self, x1, x2):
        return self.a * x1 + self.b * x2

    def check_condition(self, x1, x2) -> bool:
        if self.sign == '<=':
          return self.f_value(x1, x2) <= self.c
        elif self.sign == '=' or '==':
          return self.f_value(x1, x2) == self.c
        else:
          return self.f_value(x1, x2) >= self.c

# Функция для проверки выполнения неравенств
def Ineq(f, x, y):
    if f.sign == '<=':
        if f.y_func(x) is not None:
            return y <= f.y_func(x) if f.b > 0 else y >= f.y_func(x)
        else:
            return x <= f.x_func(y) if f.a > 0 else x >= f.x_func(y)
    elif f.sign == '>=':
        if f.y_func(x) is not None:
            return y >= f.y_func(x) if f.b > 0 else y <= f.y_func(x)
        else:
            return x >= f.x_func(y) if f.a > 0 else x <= f.x_func(y)
    else:
        return None

# Определим ограничения
b1 = LinearForm2D(2, 4, 10, '<=')
b2 = LinearForm2D(1, 0, 4, '<=')
b3 = LinearForm2D(0, 1, 2, '<=')
b4 = LinearForm2D(1, 0, 0, '>=')
b5 = LinearForm2D(0, 1, 0, '>=')

b_list = [b1, b2, b3, b4, b5]

# Построим графики прямых
plt.figure(figsize=(8, 8))
for b in b_list:
    b.prepare_plot(s=0, f=5, color=list(mcolors.BASE_COLORS.keys())[b_list.index(b)])

# Сетка для области допустимых значений
d = np.linspace(0, 5, 100)
x, y = np.meshgrid(d, d)

# Построим область допустимых решений
plt.imshow(
    (Ineq(b1, x, y) & Ineq(b2, x, y) & Ineq(b3, x, y) & Ineq(b4, x, y) & Ineq(b5, x, y)).astype(int),
    extent=(x.min(), x.max(), y.min(), y.max()), origin="lower", cmap="Greys", alpha=0.3
)

def point(f1, f2):
  d = f1.a * f2.b - f1.b * f2.a
  # print(d)
  if d == 0:
    # print('Данные прямые не пересекаются!')
    return None
  else:
    x = (f1.c * f2.b - f1.b * f2.c) / d
    y = (f1.a * f2.c - f1.c * f2.a) / d
    return (x, y)

# Добавляем настройки графика
plt.xlabel("x_1")
plt.ylabel("x_2")
plt.xlim(0, 5)
plt.ylim(0, 3)
plt.grid()
plt.title('Графическое решение с областью допустимых значений')

# Показать график
plt.show()

# Целевая функция:
F = LinearForm2D(3, 2)

# Списки значений целевой функции и точек, в которых они достигаются:
F_list = []
pt_list = []

# Условие на то, что очередная точка является допустимым решением:
pt_is_feasible = lambda x, y: Ineq(b1, x, y) & Ineq(b2, x, y) & Ineq(b3, x, y) & Ineq(b4, x, y) & Ineq(b5, x, y)

for p in list(combinations(b_list, r = 2)):
  pt = point(p[0], p[1])
  if pt is not None and pt_is_feasible(pt[0], pt[1]):
    pt_list.append(pt)
    F_list.append(F.f_value(pt[0], pt[1]))

# Поиск оптимального решения:
F_max = max(F_list) # Можно поменять на min
print(F_list, F_max)
print(pt_list[F_list.index(F_max)])
print(pt_list)
