import math as m
from dataClass import *

EPS = 1e-9


def float_equal(a, b):
    """
    Функция сравнивает числа с плавающей запятой
    """
    return m.fabs(a - b) < EPS


class Newton:
    """
    Полином Ньютона
    """

    def __init__(self, data: Data, n: int = 3):
        """
        Инициализация атрибутов класса
        """
        self.data = data
        self.n = n
        self.config_points = list()

    def get_table_value_for_x(self, x: float):
        """
        Функция ищет ближайшее к x табличное значение
        """
        diff = m.fabs(x - self.data.data_table[0].x)

        index = 0

        for ind, val in enumerate(self.data.data_table):
            if m.fabs(x - val.x) < diff:
                diff = m.fabs(x - val.x)
                index = ind

        return index

    def collect_config(self, x: float):
        """
        Функция собирает конфигурацию
        """
        index = self.get_table_value_for_x(x)

        left = right = index

        for i in range(self.n):
            if i % 2 == 0:
                if left == 0:
                    right += 1
                else:
                    left -= 1
            else:
                if right == len(self.data.data_table) - 1:
                    left -= 1
                else:
                    right += 1

        return self.data.data_table[left:right + 1]

    def get_diff_table(self, x: float):
        """
        Функция получает таблицу разделенных разностей
        для полиномов Ньютона
        """
        self.config_points = self.collect_config(x)

        count_points = len(self.config_points)

        diff_table = [[0] * count_points for _ in range(count_points)]

        for i in range(count_points):
            diff_table[i][0] = self.config_points[i].y

        for i in range(1, count_points):
            for j in range(i, count_points):
                diff_table[j][i] = \
                    (diff_table[j][i - 1] - diff_table[j - 1][i - 1]) / \
                    (self.config_points[j].x - self.config_points[j - i].x)

        return diff_table

    @staticmethod
    def get_diagonal(diff_table):
        """
        Функция получает нужные разделенные разности
        (находятся на главной диагонали)
        :return: список нужных разностей
        """
        diagonal = []

        for i in range(len(diff_table)):
            diagonal.append(diff_table[i][i])

        return diagonal

    def newton_polynom(self, x: float):
        """
        Функция строит полином Ньютона или Эрмита
        и вычисляет значение при фиксированном x
        """
        diff_table = self.get_diff_table(x)

        diff = self.get_diagonal(diff_table)

        result = diff[0]

        for i in range(1, len(diff)):
            p = diff[i]
            for j in range(i):
                p *= (x - self.config_points[j].x)
            result += p

        return result

    def get_derivative2_polynom(self, x: float, eps: float):
        """
        Метод вычисляет вторую производную полинома Ньютона
        f''(x) ≈ [f(x+h) - 2f(x) + f(x-h)] / h^2
        где h - шаг дискретизации.
        """

        fx_plus_h = self.newton_polynom(x + eps)
        fx_minus_h = self.newton_polynom(x - eps)
        fx = self.newton_polynom(x)

        return (fx_plus_h - 2 * fx + fx_minus_h) / (eps ** 2)
