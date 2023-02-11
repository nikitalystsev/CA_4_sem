import my_read
import my_print_data as my_print


def main():
    """Главная функция"""
    filename = "data"

    points = my_read.read_table(filename)

    degree = my_read.read_degree()

    x = my_read.read_x()

    my_print.print_table(points)


if __name__ == "__main__":
    main()
