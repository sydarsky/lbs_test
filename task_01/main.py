import argparse
import re
import os


def transform_output(func):
    gender_map = {
        "М": "Г-н",
        "Ж": "Г-жа"
    }

    def wrapper(*args, **kwargs):
        result = list()
        data = func(*args, **kwargs)
        for row in data:
            result.append("{} {} {}".format(gender_map[row[2]],
                                            row[0], row[1]))
        return result
    return wrapper


@transform_output
def read_from_file(filepath):
    data = None
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = f.readlines()
        data = [i.replace("\n", "").split() for i in data]
    if data is not None:
        return sorted(data, key=lambda x: int(x[3]))


@transform_output
def get_from_shell():
    rows_number = input("Введите количество строк для ввода: ")
    while not rows_number.isdigit() or rows_number == "0":
        rows_number = input("Ошибка ввода! Повторите ввод: ")
    data = [input().split() for _ in range(int(rows_number))]
    return sorted(data, key=lambda x: int(x[3]))


if __name__ == "__main__":
    line_pattern = re.compile(r'^(?P<fname>[А-Я]?[а-я]*)\s(?P<sname>[А-Я]?[а-я]*)\s(?P<sex>[МЖ])\s(?P<age>\d{1,2})$')
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", help="path to the data file")
    args = vars(ap.parse_args())
    data = list()

    if args.get("file", None) is not None:
        data = read_from_file(args['file'])
        for row in data:
            print(row)
    else:
        data = get_from_shell()
        for row in data:
            print(row)