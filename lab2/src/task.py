from spline import *
from Newton_polynom import *


class Task:
    """
    Класс для решения поставленной задачи
    """

    def __init__(self, filename: str, n: int = 3):
        """
        Инициализация атрибутов класса
        """
        # создал экземпляр класса данных,
        # прочитал таблицу с точками и
        # прочитал точку интерполирования
        self.data = Data()
        self.data.read_data(filename)
        self.data.print_data()
        self.data.read_x()

        # создал экземпляр класса Сплайн и Полинома Ньютона
        self.spline = Spline(self.data)
        self.newton = Newton(self.data, n)

        ksi2, theta2, cn_plus1 = self.calc_condition(2)
        self.spline.spline_interpolation(ksi2, theta2, cn_plus1)
        self.spline.print_spline_res()

    def calc_condition(self, condition: int):
        """
        Метод позволяет посчитать начальные значения
        прогоночных коэффициентов в зависимости от краевых условий
        """
        # посчитал начальные значения прогоночных коэффициентов
        # для третьего краевого условия
        theta2 = self.newton.get_derivative2_polynom(self.data.data_table[0].x, 1e-6)

        # нашел в общем из 3-х краевых условий значение С из фиктивного интервала
        cn_plus1 = self.newton.get_derivative2_polynom(self.data.data_table[-1].x, 1e-6)

        # из формул вытекает деление на 2
        cn_plus1 /= 2
        theta2 /= 2

        # запускаю проверку условий
        match condition:
            case 1:
                print("condition1")
                return 0, 0, 0
            case 2:
                print(f"condition2, theta2 = {theta2: .3f}")
                return 0, theta2, 0
            case _:
                print(f"condition2, theta2 = {theta2: .3f}, cn_plus_1 = {cn_plus1: .3f}")
                return 0, theta2, cn_plus1
