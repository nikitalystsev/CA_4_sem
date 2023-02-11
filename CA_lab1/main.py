import read


def main():
    """Главная функция"""
    filename = "data"

    points = read.read_table(filename)

    degree = read.read_degree()

    x = read.read_x()

    print(x)


if __name__ == "__main__":
    main()
