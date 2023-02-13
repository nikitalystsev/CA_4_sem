import math as m

EPS = 1e-9


def float_equal(a, b):
    """Функция сравнивает числа с плавающей запятой"""
    return m.fabs(a - b) < EPS


def get_table_value_for_x(points, x):
    """
    Функция ищет в таблице ближайшее значение к x
    """
    diff = m.fabs(x - points[0].x)

    index = 0

    for ind, val in enumerate(points):
        if m.fabs(x - val.x) < diff:
            diff = m.fabs(x - val.x)
            index = ind

    return index


def collect_config(points, x, n):
    """
    Функция собирает конфигурацию для дальнейшей интерполяции
    n - степень полинома
    """
    index = get_table_value_for_x(points, x)

    left = right = index
    # print("left = ", left, "right = ", right, sep='')

    for i in range(n):
        if i % 2 == 0:
            if left == 0:
                right += 1
            else:
                left -= 1
        else:
            if right == len(points) - 1:
                left -= 1
            else:
                right += 1
    # print("left = ", left, "right = ", right, sep='')
    return points[left:right + 1]


def get_points_for_hermite(points):
    """
    Функция получает таблицу точек для полинома Эрмита
    """
    new_table = []

    for point in points:
        multiplicity = 2  # кратность узла
        for i in range(multiplicity):
            new_table.append(point)

    return new_table


def get_diff_table(points):
    """
    Функция получает таблицу разделенных разностей
    для полинома Эрмита и Ньютона
    """
    count_points = len(points)

    # создаем матрицу под разделенные разности
    diff_table = [[0] * count_points for _ in range(count_points)]

    # первый столбец заполняем значениями функций из таблицы в узлах
    for i in range(count_points):
        diff_table[i][0] = points[i].y

    # получаем разделенные разности
    for i in range(1, count_points):
        for j in range(i, count_points):
            if not float_equal(points[j].x, points[j - i].x):
                diff_table[j][i] = \
                    (diff_table[j][i - 1] - diff_table[j - 1][i - 1]) / \
                    (points[j].x - points[j - i].x)
            else:
                diff_table[j][i] = points[j].derivative

    return diff_table


def get_corner(diff_table):
    """
    Функция получает диагональные элементы из таблицы интерполяции
    """
    diagonal = []

    for i in range(len(diff_table)):
        diagonal.append(diff_table[i][i])

    return diagonal


def polynom(x, diff, points):
    """
    Функция строит полином Ньютона или Эрмита
    и вычисляет значение полинома в точке x
    """
    result = diff[0]

    for i in range(1, len(diff)):
        p = diff[i]
        for j in range(i):
            p *= (x - points[j].x)
        result += p

    return result
