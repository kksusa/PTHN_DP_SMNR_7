__all__ = ['more', 'less_more', 'integer']


def more(param, min_value):
    while True:
        number = input(f"{param} ")
        if number.isdigit():
            number = int(number)
            if number > min_value:
                return number
        else:
            print("Число введено неправильно.")


def less_more(param, min_value, max_value):
    while True:
        number = input(f"{param} ")
        if number.isdigit():
            number = int(number)
            if min_value < number < max_value:
                return number
        else:
            print("Число введено неправильно.")


def integer(param):
    while True:
        number = input(f"{param} ")
        if number.isdigit():
            return int(number)
        else:
            print("Число введено неправильно.")
