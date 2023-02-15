import my_interpolation as my_interp
import my_print_data as my_print
import copy as cp

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
        config_points = my_interp.collect_config(points, x, i)
        result_newton = my_interp.polynom(config_points, x, i)
        config_points = my_interp.get_points_for_hermite(config_points)
        result_hermit = my_interp.polynom(config_points, x, i)
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

    for point in points:
        cur = point.y
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

    tmp_points.sort(key=lambda point: point.y)

    root = my_interp.polynom(tmp_points, 0, n)

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

    tmp_points = my_interp.get_points_for_hermite(tmp_points)

    tmp_points = change_column(tmp_points)

    for point in tmp_points:
        if not my_interp.float_equal(point.derivative, 0):
            point.derivative = 1 / point.derivative
        else:
            point.derivative = 0

    tmp_points.sort(key=lambda point: point.y)

    root = my_interp.polynom(tmp_points, 0, n)

    return root




