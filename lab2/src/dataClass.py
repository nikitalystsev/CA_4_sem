SIZE_TABLE = 31


class Point:
    """
    Точка
    """

    def __init__(self, x: float = 0, y: float = 0):
        """
        Инициализация атрибутов класса
        """
        self.x = x
        self.y = y


class Data:
    """
    Данные для интерполяции
    """

    def __init__(self):
        """
        Инициализация атрибутов класса
        """
        self.data_table: list[Point] = list()
        self.x = None

    def read_data(self, filename: str) -> None:
        """
        Метод считывает данные из файла
        """
        with open(filename) as file:
            for line in file:
                data = list(map(float, line.split()))
                point = Point(data[0], data[1])
                self.data_table.append(point)

    def read_x(self) -> None:
        """
        Функция считывает значение аргумента x, для которого выполняется интерполяция
        """
        if self.x is None:
            self.x = float(input("Введите значение аргумента x, "
                                 "для которого выполняется интерполяция: "))

    def del_data(self) -> None:
        """
        Метод позволяет удалить данные для интерполяции
        """
        self.data_table.clear()

    def print_data(self):
        """
        Метод выводит данные на экран
        """
        if len(self.data_table) == 0:
            print("Данные еще не были получены!")
            return

        print("|" + SIZE_TABLE * "-" + "|")
        print(f"|{'x':^15s}|{'y':^15s}|")
        print("|" + SIZE_TABLE * "-" + "|")

        for point in self.data_table:
            print("| {:^13.3f} | {:^13.3f} |".format(
                point.x,
                point.y)
            )

        print("|" + SIZE_TABLE * "-" + "|")
