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

        self.h_n = list()
        self.ksi_n = list()
        self.theta_n = list()

        self.res = None

    def calc_a_n_coef(self) -> None:
        """
        Метод позволяет вычислить первые коэффициенты сплайна
        Формула 2
        """
        # очищаем список, если ранее уже были посчитаны первые коэффициенты
        self.a_n.clear()
        # для соблюдения индексации формул, ведь 1 <= n <= N для коэффициентов
        self.a_n.append(None)

        # в цикле в соответствии с формулой 2 определяется n-й первый коэффициент
        # сплайна и добавляется в список первых коэффициентов
        for n in range(1, len(self.data.data_table)):
            an = self.data.data_table[n - 1].y
            self.a_n.append(an)

    def calc_diff_h(self) -> None:
        """
        Метод вычисляет все разности между узлами таблицы
        интерполяции
        """
        # очищаем список, если ранее были уже посчитаны разности
        self.h_n.clear()
        # для соблюдения индексации формул, ведь 1 <= n <= N для разностей
        self.h_n.append(None)

        # в цикле в соответствии с определением h как
        # разности аргументов в узлах таблицы интерполяции
        # вычисляем эти разности и добавляем в список разностей
        for n in range(1, len(self.data.data_table)):
            hn = self.data.data_table[n].x - self.data.data_table[n - 1].x
            self.h_n.append(hn)

    def calc_ksi_theta(self) -> None:
        """
        Метод позволяет вычислить прогоночные коэффициенты кси и тета при прямом ходе
        в методе прогонки
        """
        if len(self.a_n) == 0:
            print("Первые коэффициенты сплайна еще не посчитаны")
            return

        if len(self.h_n) == 0:
            print("Разности еще не посчитаны")
            return

        # сначала очистим списки
        self.ksi_n.clear()
        self.theta_n.clear()

        # добавим None для соблюдения индексации, ведь при вычислении
        # прогоночных коэффициентов 2 <= n <= N, ноль добавляется потому,
        # что кси2 и тета2 равны нулю из условия С_1 равно ноль системы 12
        self.ksi_n.extend([None, None, 0])
        self.theta_n.extend([None, None, 0])

        for n in range(2, len(self.data.data_table) - 1):
            ksi_n_plus_1 = -(self.h_n[n]) / (self.h_n[n - 1] * self.theta_n[n] + 2 * (self.h_n[n - 1] + self.h_n[n]))
            f_n = 3 * ((self.a_n[n + 1] - self.a_n[n]) / self.h_n[n] -
                       (self.a_n[n] - self.a_n[n - 1]) / self.h_n[n - 1])
            theta_n_plus_1 = (f_n - self.h_n[n - 1] * self.theta_n[n]) / \
                             (self.h_n[n - 1] * self.theta_n[n] + 2 * (self.h_n[n - 1] + self.h_n[n]))

            self.ksi_n.append(ksi_n_plus_1)
            self.theta_n.append(theta_n_plus_1)

    def calc_c_n_coef(self) -> None:
        """
        Метод вычисляет коэффициенты С_n для сплайна по формуле 13
        в обратном ходе метода прогонки
        """
        if len(self.ksi_n) == 0 or len(self.theta_n) == 0:
            print("Прогоночные коэффициенты еще не были посчитаны!")
            return

        # сначала очищаю список коэффициентов С_n, если ранее они были посчитаны
        self.c_n.clear()
        self.c_n.append(None)

        for n in range(len(self.ksi_n) - 1, 0, -1):
            if n == len(self.ksi_n) - 1:
                cn = self.ksi_n[n] * 0 + self.theta_n[n]
            else:
                cn = self.ksi_n[n + 1] * self.c_n[len(self.ksi_n) - 1 - n] + self.theta_n[n + 1]
            self.c_n.append(cn)

        self.c_n.reverse()
        self.c_n.pop()
        self.c_n.insert(0, None)

    def calc_b_n_coef(self) -> None:
        """
        Метод вычисляет значения вторых
        коэффициентов кубического сплайна
        """
        if len(self.a_n) == 0 or len(self.h_n) == 0 or len(self.c_n) == 0:
            print("Не все посчитано для определения вторых коэффициентов!")
            return

        # сначала очищаю список коэффициентов B_n, если ранее они были посчитаны
        self.b_n.clear()
        self.b_n.append(None)

        for n in range(1, len(self.data.data_table) - 1):
            bn = (self.a_n[n + 1] - self.a_n[n]) / self.h_n[n] - self.h_n[n] * ((self.c_n[n + 1] + 2 * self.c_n[n]) / 3)
            self.b_n.append(bn)

        n = len(self.data.data_table) - 1
        bn = (self.a_n[n] - self.a_n[n - 1]) / self.h_n[n] - self.h_n[n] * ((2 * self.c_n[n]) / 3)
        self.b_n.append(bn)

    def calc_d_n_coef(self) -> None:
        """
        Метод позволяет вычислить значения четвертых
        коэффициентов кубического сплайна
        """
        if len(self.c_n) == 0 or len(self.h_n) == 0:
            print("Не все посчитано для определения четвертых коэффициентов!")
            return

        # сначала очищаю список коэффициентов B_n, если ранее они были посчитаны
        self.d_n.clear()
        self.d_n.append(None)

        for n in range(1, len(self.data.data_table) - 1):
            dn = (self.c_n[n + 1] - self.c_n[n]) / (3 * self.h_n[n])
            self.d_n.append(dn)

        n = len(self.data.data_table) - 1
        dn = -(self.c_n[n] / (3 * self.h_n[n]))
        self.d_n.append(dn)

    def find_interval(self, x: float):
        """
        Метод находит наиболее подходящий интервал для интерполируемого аргумента
        """

        # Шаг 2. Проверяем, находится ли значение value за пределами диапазона аргументов
        if x < self.data.data_table[0].x:
            return 0, self.data.data_table[0].x, self.data.data_table[1].x
        elif x > self.data.data_table[-1].x:
            return len(self.data.data_table) - 1, self.data.data_table[-2].x, self.data.data_table[-1].x

        index = 0
        # Шаг 3. Ищем первый элемент в списке x, который больше value
        for i in range(len(self.data.data_table)):
            if self.data.data_table[i].x >= x:
                index = i
                break

        # Шаг 5. Возвращаем номер интервала и информацию о границах этого интервала
        return index, self.data.data_table[index - 1].x, self.data.data_table[index].x,

    def spline_interpolation(self) -> None:
        """
        Метод выполняет интерполяцию сплайном
        """
        self.calc_a_n_coef()
        # print("a_coef", len(spline.a_n), spline.a_n, end='\n\n')
        self.calc_diff_h()
        # print(len(spline.h_n), spline.h_n, end='\n\n')
        self.calc_ksi_theta()
        # print(len(spline.ksi_n), spline.ksi_n, end='\n')
        # print(len(spline.theta_n), spline.theta_n, end='\n\n')
        self.calc_c_n_coef()
        # print("c_coef", len(spline.c_n), spline.c_n, end='\n\n')
        self.calc_b_n_coef()
        # print("b_coef", len(spline.b_n), spline.b_n, end='\n\n')
        self.calc_d_n_coef()
        # print("d_coef", len(spline.d_n), spline.d_n, end='\n\n')
        num, x0, x1 = self.find_interval(self.data.x)

        self.res = \
            self.a_n[num] + self.b_n[num] * (self.data.x - x0) + self.c_n[num] * (self.data.x - x0) ** 2 + \
            self.d_n[num] * (self.data.x - x0) ** 3

    def print_spline_res(self) -> None:
        """
        Метод выводи результат интерполяции
        """

        if self.res is None:
            print("Не были совершены необходимые подсчеты!")
            return

        print(f"result = {self.res: <15.3f}")
