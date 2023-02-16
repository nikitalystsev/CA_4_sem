import src.interpolation as interpolation
import src.print_data as print_data
import src.read as read
import copy as cp
import src.point as point

SIZE_TABLE = 53


def get_table_value(x, points) -> None:
    """
    Функция получает таблицы значений при разных степенях полиномов
    и при фиксированном x
    :param x: точка интерполирования
    :param points: считанный список точек
    :return:
    """
    print("|" + SIZE_TABLE * "-" + "|")
    print(f"| {'Степень полинома':^17s}|{'Полином Ньютона':^17s}|{'Полином Эрмита':^16s}|")
    print("|" + SIZE_TABLE * "-" + "|")

    for i in range(1, 6):
        config_points = interpolation.collect_config(points, x, i)
        result_newton = interpolation.polynom(config_points, x, i)
        config_points = interpolation.get_points_for_hermite(config_points)
        result_hermit = interpolation.polynom(config_points, x, i)
        print("| {:^16d} | {:^15.7f} | {:^14.7f} |".format(
            i,
            result_newton,
            result_hermit)
        )

    print("|" + SIZE_TABLE * "-" + "|")


def is_change_sign(points) -> bool:
    """
    Факт наличия корня у функции устанавливается по наличию 
    смены знака у функции при продвижении по строкам таблицы
    :param points: считанный список точек
    :return: True - знак меняется, False в противном случае
    """
    prev = points[0].y

    for dot in points:
        cur = dot.y
        if prev * cur < 0:
            return True
        prev = cur

    return False


def change_column(points):
    """
    Функция меняет местами столбцы с аргументом функции и ее значением
    :param points: считанный список точек
    :return: преобразованный список точек
    """

    for i in range(len(points)):
        points[i].x, points[i].y = points[i].y, points[i].x

    return points


def get_newton_root(points, n):
    """
    Функция вычисляет корень табличной функции с
    помощью обратной интерполяции полинома Ньютона
    :param points: считанный список точек
    :param n: степень полинома
    :return: корень функции
    """
    tmp_points = cp.deepcopy(points)

    tmp_points = change_column(tmp_points)

    tmp_points.sort(key=lambda dot: dot.y)

    root = interpolation.polynom(tmp_points, 0, n)

    return root


def get_hermit_root(points, n):
    """
    Функция вычисляет корень табличной функции с
    помощью обратной интерполяции полинома Эрмита
    :param points: считанный список точек
    :param n: степень полинома
    :return: корень функции
    """
    tmp_points = cp.deepcopy(points)

    tmp_points = interpolation.get_points_for_hermite(tmp_points)

    tmp_points = change_column(tmp_points)

    for dot in tmp_points:
        if not interpolation.float_equal(dot.derivative, 0):
            point.derivative = 1 / dot.derivative
        else:
            point.derivative = 0

    tmp_points.sort(key=lambda dot: dot.y)

    root = interpolation.polynom(tmp_points, 0, n)

    return root


# С помощью интерполяции перестроить приведенные табличные представления
# функций к новой таблице, в которой содержится зависимость разности функций y(x) из
# (1) и (2) от фиксированного набора значений аргумента x, например, такого, как во второй
# таблице, или любого другого из рассматриваемого интервала. Затем применить процедуру
# обратной интерполяции.

# выбираем множество Х для двух функций (удобно взять Х-сы их 2-й таблицы, поскольку Y для них известны)
# Чтобы найти разность Y тебе нужно из значений Y второй таблицы
# вычесть значения Y из первой таблицы, но с помощью интерполяции в тех же x

def func(points1, points2, n):
    new_points1 = []

    for i in range(len(points2)):
        # найти значение при тех же Х
        tmp_points = cp.deepcopy(points1)
        result_newton = interpolation.polynom(tmp_points, points2[i].x, n)
        new_points1.append(point.Point(points1[i].x, result_newton, 0))

    return new_points1


def get_subtract_table(points1, points2):
    table = []

    for i in range(len(points2)):
        table.append(point.Point(points2[i].x, points1[i].y - points2[i].y, 0))

    return table


def get_system_root(n):
    """
    Функция находит корень системы
    :param n: степень полинома Ньютона
    :return: корень
    """
    points1 = read.read_system_table("../data/system1.txt")

    # print("Первая считанная таблица X(Y):")
    # print_data.print_table(points1)

    points2 = read.read_system_table("../data/system2.txt")

    # смена столбцов
    points1 = change_column(points1)

    print("Первая считанная таблица Y(X):")
    print_data.print_table(points1)

    print("Вторая считанная таблица Y(X):")
    print_data.print_table(points2)

    points1 = func(points1, points2, n)

    print("Интерполированная первая таблица (Ординаты интерполированы для абсцисс второй таблицы):")
    print_data.print_table(points1)

    table = get_subtract_table(points1, points2)

    print("Таблица с разностями абсцисс двух таблиц и ординат второй таблицы")
    print_data.print_table(table)

    table = change_column(table)

    print("Таблица с разностями абсцисс двух таблиц и ординат второй таблицы (столбцы поменяны):")
    print_data.print_table(table)

    root = get_newton_root(table, n)

    return root
