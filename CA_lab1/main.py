import my_read


def main():
    """Главная функция"""
    filename = "data"

    points = my_read.read_table(filename)

    degree = my_read.read_degree()

    x = my_read.read_x()

    print(x)


if __name__ == "__main__":
    main()
