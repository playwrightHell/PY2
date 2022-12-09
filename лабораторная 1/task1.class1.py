import doctest


class House:
    def __int__(self, owner_name: str, height: int):
        """
        Объект Дом: создание и подготовка к работе

        :param owner_name: Имя владельца
        :param height: Высота здания в метрах
        """

        if not isinstance(owner_name, str):
            raise TypeError("Имя должно быть типа str")
        self.owner_name = owner_name

        if not isinstance(height, int):
            raise TypeError("Высота толжна быть типа int")
        if height < 0:
            raise ValueError("Высота не может быть отрицательной")
        self.height = height

    def elevator_availability(self) -> bool:
        """
        Проверка на наличие в доме лифта

        :return: есть ли в доме лифт
        """
        ...

    def house_age(self, age: [int, float]):
        """
        Выяснение, сколько дому лет.
        :param age: Возраст, собственно
        :raise ValueError: Если возраст отрицательный, возвращается ошибка
        :raise TypeError: Если введен неверный тип данных, возвращается ошибка
        :return: Возраст дома
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
