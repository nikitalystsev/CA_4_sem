from my_point import *
from dataClass import *


class Spline:
    """
    Сплайн
    """

    def __init__(self, data: Data):
        """
        Инициализация атрибутов класса
        """
        self.data = data
        self.a_n = list()
        self.b_n = list()
        self.c_n = list()
        self.d_n = list()

    def calc_a_n_coef(self) -> None:
        """
        Метод позволяет вычислить первые коэффициенты сплайна
        Формула 2
        """
        # очищаем список, если ранее уже были посчитаны первые коэффициенты
        self.a_n.clear()

        # в цикле в соответствии с формулой 2 определяется n-й первый коэффициент
        # сплайна и добавляется в список первых коэффициентов
        for point in self.data.data_table:
            an = point.y
            self.a_n.append(an)
