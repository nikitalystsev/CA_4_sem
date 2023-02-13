import my_read
import my_print_data as my_print
import my_interpolation as my_interp


def main():
    """Главная функция"""
    filename = "data.txt"

    points = my_read.read_table(filename)

    degree = my_read.read_degree()

    x = my_read.read_x()

    my_print.print_table(points)

    points = my_interp.collect_config(points, x, degree)
    # my_print.print_table(points)

    diff_table_newton = my_interp.get_diff_table(points)
    diff_newton = my_interp.get_corner(diff_table_newton)
    my_print.print_matrix(diff_table_newton)
    new_table = my_interp.get_points_for_hermite(points)
    # my_print.print_table(new_table)
    diff_table_hermit = my_interp.get_diff_table(new_table)
    diff_hermit = my_interp.get_corner(diff_table_hermit)
    my_print.print_matrix(diff_table_hermit)
    result_newton = my_interp.polynom(x, diff_newton, points)

    result_hermit = my_interp.polynom(x, diff_hermit, new_table)

    print("newton:", result_newton, "hermit:", result_hermit, sep='\n')


if __name__ == "__main__":
    main()
