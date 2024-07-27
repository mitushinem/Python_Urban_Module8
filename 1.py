def add_everything_up(a, b):
    try:
        if isinstance(a and b, int) or isinstance(a and b, float):
            return a + b
        else:
            raise TypeError

    except TypeError as exc:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
