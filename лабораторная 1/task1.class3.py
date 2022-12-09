import doctest


class Room:
    def __int__(self, capacity: int, free_space: int):
        """
        Объект Комната: создание и подготовка к работе

        :param capacity: Вместительность комнаты
        :param free_space: Свободное место в комнате
        """

        if not isinstance(capacity, int):
            raise TypeError("Вместимость должна идти в формате int")
        if capacity < 0:
            raise ValueError("Вместимость не должна быть отрицательной")
        self.capacity = capacity

        if not isinstance(free_space, int):
            raise TypeError("Свободное место должно идти в формате int")
        if free_space < 0:
            raise ValueError("Свободное место не может быть отрицательным")
        self.free_space = free_space

    def is_room_empty(self) -> bool:
        """
        Проверка, есть ли в комнате люди.

        :return: Есть ли в комнате люди
        """
    def invite_someone(self, person: float) -> None:
        """
        "Добавление" людей в комнату.

        :param person: Вошедшие люди
        :raise ValueError: ошибка, если пытаются запихать в комнату людей, которые не влезают по вместимости
        """

    def expel_someone(self, person_expelled: float) -> None:
        """
        Изгнание людей из комнаты.

        :param person_expelled: количество человек, которые были выгнаны из комнаты
        :raise ValueError: ошибка, если пытаются выгнать больше людей, чем находится в комнате

        :return: Сколько людей в итоге выгнали
        """


if __name__ == "__main__":
    doctest.testmod()
