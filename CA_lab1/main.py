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

    new_table = my_interp.get_points_table_for_hermite(points)

    diff_table_hermit = my_interp.get_diff_table_for_hermite(new_table)

    my_print.print_matrix(diff_table_hermit)

    diff_hermit = my_interp.get_corner(diff_table_hermit)

    result = my_interp.newton_polynom(0.6, diff, points)
    result2 = my_interp.newton_polynom(0.6, diff_hermit, new_table)

    print("newton:", result, "hermit:", result2, sep='\n')


if __name__ == "__main__":
    main()
