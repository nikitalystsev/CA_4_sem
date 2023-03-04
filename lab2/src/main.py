from spline import *
from dataClass import *
from Newton_polynom import *


def main() -> None:
    """
    Главная функция
    """
    data = Data()
    data.read_data("../data/data1.txt")
    data.print_data()
    data.read_x()

    newton = Newton(data, 3)
    y_der2 = newton.get_derivative_polynom()
    print(y_der2)
    spline = Spline(data)
    spline.spline_interpolation()
    spline.print_spline_res()


if __name__ == "__main__":
    main()
