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


if __name__ == "__main__":
    main()
