
class Games:
    """ Базовый класс Игры, включающий в себя название игры и ее правила. """
    def __init__(self, name: str, rules: str):
        self.name = name
        self.rules = rules

    def __str__(self) -> str:
        return f"Игра: {self.name}. Правила: {self.rules}"

    def __repr__(self) -> str:
        return f'Games(name={self.name!r}, rules={self.rules!r})'


class BoardGames(Games):
    """
    Дочерний класс Настольные игры. Включает в себя также параметр "игровые фигурки"
    """
    def __init__(self, name: str, rules: str, figures: int):
        super().__init__(name, rules)
        """
        Определение количества фигурок, использующихся в игре.
        """
        if isinstance(figures, int):
            if figures > 0:
                self.figures = figures
            else:
                raise AttributeError(f'error count of figures')
        else:
            raise AttributeError(f'error type of figures')

    def needed_figures(self, figures: int) -> int:
        """
        Определение необходимого кол-ва фигурок в один ход
        :param figures:
        :return: figures = int
        """

    """
    Перегрузка __str__, __repr__, т.к. добавляется параметр figures.
    """
    def __str__(self) -> str:
        return f"Игра {self.name}. Правила {self.rules}. Кол-во фигурок {self.figures}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, rules={self.rules!r}, figures={self.figures!r})"


class ComputerGames(Games):
    def __init__(self, name: str, rules: str, duration: float):
        super().__init__(name, rules)
        if isinstance(duration, float):
            if duration > 0:
                self.duration = duration
            else:
                raise AttributeError(f'error count of duration')
        else:
            raise AttributeError(f'error type of duration')

    def one_game_duration(self, duration: float) -> float:
        """
        Определение, сколько длится одна партия.
        :param duration:
        :return: duration = float
        """
    """
    Перегрузка __str__, __repr__, т.к. добавляется параметр duration.
    """
    def __str__(self) -> str:
        return f"Игра {self.name}. Правила {self.rules}. Продолжительность {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, rules={self.rules!r}, duration={self.duration!r})"


if __name__ == "__main__":
    pass
