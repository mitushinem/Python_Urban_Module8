class Car:
    def __init__(self, model, vin, number):
        self.model = model
        self.__number = number if self.__is_valid_numbers(number) else None
        self.__vin = vin if self.__is_valid_vin(vin) else None

    @staticmethod
    def __is_valid_vin(vin_number):
        try:
            if not isinstance(vin_number, int):
                raise IncorrectVinNumber('Некорректный тип vin номер')
            if vin_number < 1000000 or vin_number > 9000000:
                raise IncorrectCarNumbers('Неверный диапазон для vin номера')
        except IncorrectVinNumber:
            raise
        except IncorrectCarNumbers:
            raise
        else:
            return True

    @staticmethod
    def __is_valid_numbers(numbers):
        try:
            if not isinstance(numbers, str):
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            if not len(numbers) == 6:
                raise IncorrectCarNumbers('Неверная длина номера')
        except IncorrectVinNumber:
            raise
        except IncorrectCarNumbers:
            raise
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
