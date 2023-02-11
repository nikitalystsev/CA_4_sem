import my_read
import my_print_data as my_print
import my_interpolation as my_interp


def main():
    """Главная функция"""
    filename = "data2.txt"

    points = my_read.read_table(filename)

    # degree = my_read.read_degree()
    #
    # x = my_read.read_x()

    my_print.print_table(points)

    diff_table = my_interp.get_diff_table(points)

    my_print.print_matrix(diff_table)

    diff = my_interp.get_corner(diff_table)

    result = my_interp.newton_polynom(0.6, diff, points)

    print(result)


if __name__ == "__main__":
    main()
