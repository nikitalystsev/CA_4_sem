def get_diff_table(points_table):
    """Функция получает таблицу разделенных разностей для полинома Ньютона"""
    count_points = len(points_table)

    # создаем матрицу под разделенные разности
    diff_table = [[0] * count_points for _ in range(count_points)]

    # первый столбец заполняем значениями функций из таблицы в узлах
    for i in range(count_points):
        diff_table[i][0] = points_table[i][1]

    # получаем разделенные разности
    for i in range(1, count_points):
        for j in range(i, count_points):  # обходим под главной диагональю
            # j-i определяет диагональные элементы
            diff_table[j][i] = \
                (diff_table[j][i - 1] - diff_table[j - 1][i - 1]) / \
                (points_table[j][0] - points_table[j - i][0])

    return diff_table


def get_corner(diff_table):
    """
    Функция получает диагональные элементы из таблицы интерполяции
    """
    diagonal = []

    for i in range(len(diff_table)):
        diagonal.append(diff_table[i][i])

    return diagonal


def newton_polynom(x, diff, points_table):
    """
    Функция строит полином Ньютона
    и вычисляет значение полинома в точке x
    """
    y0 = diff[0]

    result = y0
    for i in range(1, len(diff)):
        p = diff[i]
        for j in range(i):
            p *= (x - points_table[j][0])
        result += p

    return result


def get_points_table_for_hermite(points_table):
    """
    Функция получает таблицу точек для полинома Эрмита
    """
    new_table = []

    for point in points_table:
        multiplicity = len(point) - 1  # кратность узла
        for i in range(multiplicity):
            new_table.append(point)

    return new_table


def get_diff_table_for_hermite(points_table):
    """
    Функция получает таблицу разделенных разностей для полинома Эрмита
    """
    count_points = len(points_table)

    # создаем матрицу под разделенные разности
    diff_table = [[0] * count_points for _ in range(count_points)]

    # первый столбец заполняем значениями функций из таблицы в узлах
    for i in range(count_points):
        diff_table[i][0] = points_table[i][1]

    # получаем разделенные разности
    for i in range(1, count_points):
        for j in range(i, count_points):  # обходим под главной диагональю
            # j-i определяет диагональные элементы
            if points_table[j][0] - points_table[j - i][0] != 0:
                diff_table[j][i] = \
                    (diff_table[j][i - 1] - diff_table[j - 1][i - 1]) / \
                    (points_table[j][0] - points_table[j - i][0])
            else:
                diff_table[j][i] = points_table[j][2]

    return diff_table
