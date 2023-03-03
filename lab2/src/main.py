from spline import *
from dataClass import *


def main() -> None:
    """
    Главная функция
    """
    data = Data()

    data.read_data("../data/data1.txt")

    data.print_data()

    spline = Spline(data)
    spline.calc_a_n_coef()
    print(spline.a_n)


if __name__ == "__main__":
    main()
