import os
import argparse


def count_words(func):

    def wrapper(*args, **kwargs):
        counters = dict()
        source_data, search_data = func(*args, **kwargs)
        for string in search_data:
            counters[string] = source_data.count(string)
        return counters

    return wrapper


@count_words
def read_from_file(filepath):
    source_data, search_data = list(), list()
    list_to_append = source_data
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            for line in f.readlines()[1:]:
                line = line.strip()
                if not line.isdigit():
                    list_to_append.append(line)
                else:
                    list_to_append = search_data

    return source_data, list(set(search_data))


@count_words
def get_from_shell():

    rows_number = input("Введите количество строк исходных данных: ")
    while not rows_number.isdigit() or rows_number == "0":
        rows_number = input("Ошибка ввода! Повторите ввод: ")
    source_data = [input() for _ in range(int(rows_number))]

    rows_number = input("Введите количество строк для поиска: ")
    while not rows_number.isdigit() or rows_number == "0":
        rows_number = input("Ошибка ввода! Повторите ввод: ")
    search_data = [input() for _ in range(int(rows_number))]

    return source_data, list(set(search_data))


def count_search_data(source_data, search_data):
    counters = dict()
    for string in search_data:
        counters[string] = source_data.count(string)
    return counters


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", help="path to the data file")
    args = vars(ap.parse_args())
    data = list()

    if args.get("file", None) is not None:
        counters = read_from_file(args['file'])
        for k, v in counters.items():
            print("{}: {}".format(k, v))
    else:
        counters = get_from_shell()
        for k, v in counters.items():
            print("{}: {}".format(k, v))
