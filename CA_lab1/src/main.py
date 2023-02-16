import src.read
import src.print_data
import src.interpolation
import tasks

SIZE = 75


def main():
    """
    Главная функция
    """

    root = tasks.get_system_root(4)
    print("root of system = ", root)
    # filename = "data.txt"
    #
    # print("\n" + SIZE * "-")

    # print("Считанная таблица:")

    # points = my_read.read_table(filename)
    # # my_print.print_table(points)
    #
    # if not tasks.is_change_sign(points):
    #     print("Функция не имеет корней")
    #
    # root_newton = tasks.get_newton_root(points, 7)
    # root_hermit = tasks.get_hermit_root(points, 10)
    # print("hermit root = ", root_hermit)
    # print("newton root = ", root_newton)

    # degree = my_read.read_degree()
    # x = my_read.read_x()
    #
    # print("\n" + SIZE * "-")
    #
    # config_points = my_interp.collect_config(points, x, degree)
    # result_newton = my_interp.polynom(config_points, x, degree)
    #
    # config_points = my_interp.get_points_for_hermite(config_points)
    # result_hermit = my_interp.polynom(config_points, x, degree)
    #
    # print(f"Степень полинома Ньютона n = {degree}, y({x:<.3f}) = {result_newton:<.7f}")
    # print(f"Степень полинома Эрмита  n = {degree}, y({x:<.3f}) = {result_hermit:<.7f}")
    #
    # print("\n" + SIZE * "-")
    #
    # print("Таблица значений y(x) при степенях "
    #       "полиномов Ньютона и Эрмита при x = {:<13.3f}".format(x))
    # tasks.get_table_value(x, points)
    #
    # print("\n" + SIZE * "-")


if __name__ == "__main__":
    main()
