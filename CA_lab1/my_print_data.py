SIZE_TABLE = 47


def print_table(points_table):
    """Функция выводит на экран считанные из файла табличные значения точек"""
    print("|" + SIZE_TABLE * "-" + "|")
    print(f"|{'x':^15s}|{'y':^15s}|{'y,':^15s}|")
    print("|" + SIZE_TABLE * "-" + "|")

    for i in range(len(points_table)):
        print("| {:^13.3f} | {:^13.3f} | {:^13.3f} |".format(
            points_table[i][0],
            points_table[i][1],
            points_table[i][2])
        )

    print("|" + SIZE_TABLE * "-" + "|")
