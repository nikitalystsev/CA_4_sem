from spline import *
from dataClass import *


def main() -> None:
    """
    Главная функция
    """
    data = Data()

    data.read_data("../data/data1.txt")

    data.print_data()

    data.read_x()

    spline = Spline(data)

    spline.spline_interpolation()

    spline.print_spline_res()


if __name__ == "__main__":
    main()
