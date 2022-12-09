import doctest


class Casket:
    def __int__(self, capacity: int, free_space: int):
        """
        Объект Шкатулка: создание и подготовка к работе

        :param capacity: вместимость
        :param free_space: свободное место
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

    def casket_material(self) -> str:
        """
        Определение материала, из которого сделана шкатулка
        :return: "Строчка, содержащая информацию о материале"
        """

    def is_empty_casket(self) -> bool:
        """
        Ф-я, проверяющая, является ли шкатулка пустой
        :return: Является ли шкатулка пустой
        """


if __name__ == "__main__":
    doctest.testmod()
